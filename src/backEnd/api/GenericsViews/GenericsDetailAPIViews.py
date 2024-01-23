from api.serializers import (
    StudyPlanSerializer,
    UserSerializerPrivate,
    studyPlanDetailSerializer,
    ActiveCourseSerializerComplete,
    SubscriptionSerializerComplete,
    PaymentSubscriptionSerializer,
    BankAccountSerializer,
    SchoolSerializer
)
from permissions.AppPermissionsProfile import IsNotUserAS
from rest_framework.generics import RetrieveAPIView

from accounts.models import CustomUserModel as UserModel
from accounts.models import BankAccount
from studyPlans.models import StudyPlan, StudyPlanDetail
from activeCourses.models import ActiveCourse
from subscriptions.models import Subscription, Payment
from schools.models import School


class BaseRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsNotUserAS]

    def get_permissions(self):
        permissions = []
        for perm in self.permission_classes:
            if (perm.__name__ == 'IsNotUserAS'):
                permissions.append(perm(role_exclude='guest'))
            else:
                permissions.append(perm())

        return permissions


# /api/bank-account/<int:pk>/ -> api-detail-bank-account
# class DetailBankAccountAPIView(BaseRetrieveAPIView):
class DetailBankAccountAPIView(BaseRetrieveAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    #permission_classes = [IsNotUserAS]


# /api/study-plans/<int:pk>/ -> api-study-plan
# class DetailStudyPlanAPIView(BaseRetrieveAPIView):
class DetailStudyPlanAPIView(RetrieveAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    #permission_classes = [IsNotUserAS]


# /api/study-plan-detail/<int:p>/ -> api-detail-study-plan
# class DetailStudyPlanDetailAPIView(BaseRetrieveAPIView):
class DetailStudyPlanDetailAPIView(RetrieveAPIView):
    queryset = StudyPlanDetail.objects.all()
    serializer_class = studyPlanDetailSerializer
    #permission_classes = [IsNotUserAS]


# /api/user/<int:pk>/ -> api-user-data
# class UserDataAPIView(BaseRetrieveAPIView):
class UserDataAPIView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerPrivate
    #permission_classes = [IsNotUserAS]


# /api/active-courses/<int:pk>/ -> api-active-course
# class ActiveCourseAPIView(BaseRetrieveAPIView):
class ActiveCourseAPIView(RetrieveAPIView):
    queryset = ActiveCourse.objects.all()
    serializer_class = ActiveCourseSerializerComplete
    #permission_classes = [IsNotUserAS]


# /api/subscription/<int:pk>/ -> api-subscription
# class SubscriptionAPIView(BaseRetrieveAPIView):
class SubscriptionAPIView(RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializerComplete
    #permission_classes = [IsNotUserAS]


# /api/payments-subscription/<int:pk>/ -> api-payments-subscription
# class PaymentAPIView(BaseRetrieveAPIView):
class PaymentAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSubscriptionSerializer
    #permission_classes = [IsNotUserAS]


# /api/school/<int:pk>/ -> api-school-detail
# class SchoolAPIView(BaseRetrieveAPIView):
class SchoolAPIView(RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    #permission_classes = [IsNotUserAS]
