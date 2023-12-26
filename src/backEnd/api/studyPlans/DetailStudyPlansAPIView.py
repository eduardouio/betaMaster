from rest_framework.generics import RetrieveAPIView
from studyPlans.models import StudyPlan
from api.serializers import StudyPlanSerializer


class DetailStudyPlansAPIView(RetrieveAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
