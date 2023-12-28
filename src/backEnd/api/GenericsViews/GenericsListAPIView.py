from api.serializers import (
    StudyPlanSerializer,
    UserSerializerPrivate,
    studyPlanDetailSerializer,
    ActiveCourseSerializer,
    SubscriptionSerializer,
    PaymentSubscriptionSerializer
)
from permissions.AppPermissionsProfile import IsNotUserAS
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from accounts.models import CustomUserModel as UserModel
from studyPlans.models import StudyPlan, StudyPlanDetail
from activeCourses.models import ActiveCourse
from subscriptions.models import Subscription


class BasePagination(PageNumberPagination):
    page_size = 20


# /api/courses/<int:pk>/ -> api-study-plan
class ListActiveCourseAPIView(ListAPIView):
    queryset = ActiveCourse.objects.all()
    serializer_class = ActiveCourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BasePagination

    def get_queryset(self):
        return ActiveCourse.objects.filter(user=self.kwargs['pk']).order_by('pk')

    def paginate_queryset(self, queryset):
        self.page_size = 10
        return super().paginate_queryset(queryset)


# /api/study-plans/ -> api-list-study-plans
class ListStudyPlanAPIView(ListAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    pagination_class = BasePagination

    def get_queryset(self):
        role = self.kwargs['role_name']
        return UserModel.objects.filter(role=role).order_by('pk')
