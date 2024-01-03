from api.serializers import (
    StudyPlanSerializer,
    UserSerializerPrivate,
    ActiveCourseSerializer,
    SubscriptionSerializer,
    SchoolSerializer,
)

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from accounts.models import CustomUserModel as UserModel
from studyPlans.models import StudyPlan
from activeCourses.models import ActiveCourse
from subscriptions.models import Subscription
from schools.models import School


class BasePagination(PageNumberPagination):
    page_size = 10


# /api/subscriptions/<int:pk>/ -> api-subscriptions-list
class ListSubscriptionAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    pagination_class = BasePagination


# /api/schools -> api-schools-list
class ListSchoolsAPIView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = BasePagination


# /api/active-courses/ -> api-active-courses-list
class ListActiveCourseAPIView(ListAPIView):
    queryset = ActiveCourse.objects.all()
    serializer_class = ActiveCourseSerializer
    pagination_class = BasePagination


# /api/study-plans/ -> api-list-study-plans
class ListStudyPlanAPIView(ListAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    pagination_class = BasePagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for i in response.data['results']:
            i.pop('details', None)

        return response


# /api/users-by-role/<str:role>/ -> api-users-by-role-list
class ListUserByRoleAPIView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerPrivate
    pagination_class = BasePagination

    def get_queryset(self):
        role = self.kwargs['role_name']
        return UserModel.objects.filter(role=role).order_by('pk')
