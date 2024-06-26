from api.serializers import (
    StudyPlanSerializer,
    UserSerializerPrivate,
    ActiveCourseSerializerComplete,
    ActiveCourseSerializer,
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
    page_size = 100


# /api/subscriptions/<int:pk>/ -> api-subscriptions-list
class ListSubscriptionAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializerComplete
    pagination_class = BasePagination


# /api/user/personal-reference/<int: id_user>/`
class ListPersonalReferenceAPIView(ListAPIView):
    queryset = PersonalReferences.objects.all()
    serializer_class = PersonalReferencesSerializer

    def get_queryset(self):
        id_user = self.kwargs['pk']
        user = UserModel.objects.get(pk=id_user)
        return PersonalReferences.objects.filter(id_user=user)


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
        roles = {
            'student': 'ESTUDIANTE',
            'teacher': 'PROFESOR',
            'school': 'COLEGIO'
        }
        role = self.kwargs.get('role_name')
        return UserModel.objects.filter(
            role=roles[role], is_aproved='APROBADO'
        ).order_by('pk')


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

    def get_queryset(self):
        teacher = UserModel.objects.get(pk=self.kwargs['id_teacher'])
        active_courses = ActiveCourse.objects.filter(teacher=teacher)
        return [i.student for i in active_courses]


# /api/user/schools-by-teacher/<int:id_teacher>/
class listSchoolsByTeacherAPIView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        teacher = UserModel.objects.get(pk=self.kwargs['id_teacher'])
        active_courses = ActiveCourse.objects.filter(teacher=teacher)
        schools = [i.id_school for i in active_courses]
        return schools


# /api/user/courses-by-user/<int:id_teacher>/
class ListActiveCoursesByUser(ListAPIView):
    queryset = ActiveCourse.objects.all()
    serializer_class = ActiveCourseSerializerComplete

    def get_queryset(self):
        user = UserModel.objects.get(pk=self.kwargs['id_user'])
        if user.role == 'ESTUDUANTE':
            return ActiveCourse.objects.filter(student=user)

        return ActiveCourse.objects.filter(teacher=user)


# /api/user/students-by-school-teacher/<int:id_user>/<int:id_school>/
class ListStudentsBySchoolTeacherAPIView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerPublic

    def get_queryset(self):
        teacher = UserModel.objects.get(pk=self.kwargs['id_user'])
        school = School.objects.get(pk=self.kwargs['id_school'])
        active_courses = ActiveCourse.objects.filter(
            teacher=teacher, id_school=school
        )
        return [i.student for i in active_courses]
