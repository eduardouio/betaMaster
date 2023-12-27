from api.serializers import StudyPlanSerializer, studyPlanDetailSerializer
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView)
from studyPlans.models import StudyPlan, StudyPlanDetail
from permissions.AppPermissionsProfile import IsNotUserAS
from rest_framework.permissions import IsAuthenticated


# /api/study-plans/<int:pk>/ -> api-study-plan
class DetailStudyPlanAPIView(RetrieveAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [IsNotUserAS, IsAuthenticated]

    def get_permissions(self):
        permissions = []
        for perm in self.permission_classes:
            if (perm.__name__ == 'IsNotUserAS'):
                permissions.append(perm(role_exclude='guest'))
            else:
                permissions.append(perm())

        return permissions


# /api/study-plan-detail/<int:p>/ -> api-detail-study-plans
class DetailStudyPlanDetailAPIView(RetrieveAPIView):
    queryset = StudyPlanDetail.objects.all()
    serializer_class = studyPlanDetailSerializer
