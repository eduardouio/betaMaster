from accounts.models import BankAccount
from accounts.models import CustomUserModel as UserModel
from accounts.models import PersonalReferences
from api.serializers import (BankAccountSerializer,
                             PersonalReferencesSerializer, StudyPlanSerializer,
                             UserSerializerPublic, studyPlanDetailSerializer)
from permissions.AppPermissionsProfile import IsNotUserAS
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from studyPlans.models import StudyPlan, StudyPlanDetail


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
    serializer_class = UserSerializerPublic
    permission_classes = [IsNotUserAS, IsAuthenticated]
