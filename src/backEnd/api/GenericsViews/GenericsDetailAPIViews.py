from api.serializers import (
    StudyPlanSerializer,
    UserSerializerPrivate,
    studyPlanDetailSerializer,
    ActiveCourseSerializer,
    SubscriptionSerializer,
    PaymentSubscriptionSerializer
)
from permissions.AppPermissionsProfile import IsNotUserAS
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUserModel as UserModel
from studyPlans.models import StudyPlan, StudyPlanDetail
from activeCourses.models import ActiveCourse
from subscriptions.models import Subscription


class BaseRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsNotUserAS, IsAuthenticated]

    def get_permissions(self):
        permissions = []
        for perm in self.permission_classes:
            if (perm.__name__ == 'IsNotUserAS'):
                permissions.append(perm(role_exclude='guest'))
            else:
                permissions.append(perm())

        return permissions


# /api/study-plans/<int:pk>/ -> api-study-plan
class DetailStudyPlanAPIView(BaseRetrieveAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [IsNotUserAS, IsAuthenticated]


# /api/study-plan-detail/<int:p>/ -> api-detail-study-plan
class DetailStudyPlanDetailAPIView(BaseRetrieveAPIView):
    queryset = StudyPlanDetail.objects.all()
    serializer_class = studyPlanDetailSerializer
    permission_classes = [IsNotUserAS, IsAuthenticated]


# /api/user/<int:pk>/ -> api-user-data
class UserDataAPIView(BaseRetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerPrivate
    permission_classes = [IsNotUserAS, IsAuthenticated]


# /api/active-courses/<int:pk>/ -> api-active-course
class ActiveCourseAPIView(BaseRetrieveAPIView):
    queryset = ActiveCourse.objects.all()
    serializer_class = ActiveCourseSerializer
    permission_classes = [IsNotUserAS, IsAuthenticated]


# /api/subscription/<int:pk>/ -> api-subscription
class SubscriptionAPIView(BaseRetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsNotUserAS, IsAuthenticated]


# /api/payments-subscription/<int:pk>/ -> api-payments-subscription
class PaymentAPIView(BaseRetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = PaymentSubscriptionSerializer
    permission_classes = [IsNotUserAS, IsAuthenticated]