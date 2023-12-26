from api.serializers import StudyPlanSerializer, studyPlanDetailSerializer
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView)
from studyPlans.models import StudyPlan, StudyPlanDetail


# /api/study-plans/<int:pk>/ -> api-study-plan
class DetailStudyPlanAPIView(RetrieveAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer


# /api/study-plan-detail/<int:p>/ -> api-detail-study-plans
class DetailStudyPlanDetailAPIView(RetrieveAPIView):
    queryset = StudyPlanDetail.objects.all()
    serializer_class = studyPlanDetailSerializer
