from api.serializers import (
    StudyPlanSerializer,
    UserSerializerPrivate,
    ActiveCourseSerializerComplete,
    SubscriptionSerializerComplete,
    SchoolSerializer,
    PersonalReferencesSerializer,
    BankAccountSerializer,
    UserSerializerPublic
)

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from accounts.models import (
    CustomUserModel as UserModel,
    PersonalReferences,
    BankAccount
)
from studyPlans.models import StudyPlan
from activeCourses.models import ActiveCourse
from subscriptions.models import Subscription
from schools.models import School


class BasePagination(PageNumberPagination):
    page_size = 15


# /api/subscriptions/<int:pk>/ -> api-subscriptions-list
class ListSubscriptionAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializerComplete
    pagination_class = BasePagination


# /api/user/personal-reference/<int: id_user>/`
class ListPersonalReferenceAPIView(ListAPIView):
    queryset = PersonalReferences.objects.all()
    serializer_class = PersonalReferencesSerializer


# /api/schools -> api-schools-list
class ListSchoolsAPIView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = BasePagination


# /api/active-courses/ -> api-active-courses-list
class ListActiveCourseAPIView(ListAPIView):
    queryset = ActiveCourse.objects.all()
    serializer_class = ActiveCourseSerializerComplete
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


# /api/user/banks-accounts/<int:id_user>
class ListUserBanksAccountsAPIView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        id_user = self.kwargs['id_user']
        user = UserModel.objects.get(pk=id_user)
        return BankAccount.objects.filter(id_user=user)


# /api/user/students-by-teacher/<int:id_teacher>/
class ListStudentsByTeacherAPIView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerPublic
    pagination_class = BasePagination

    def get_queryset(self):
        teacher = UserModel.objects.get(pk=self.kwargs['id_teacher'])
        active_courses = ActiveCourse.objects.filter(teacher=teacher)
        return [i.student for i in active_courses]
