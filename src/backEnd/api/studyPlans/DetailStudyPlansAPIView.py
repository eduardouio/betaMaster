from rest_framework.generic import RetriveAPIView
from studyPlans.models import StudyPlans
from api.serializers import StudyPlanSerializer


class DetailAPIView(RetriveAPIView):
    queryset = StudyPlans.objects.all()
    serializer_class = StudyPlanSerializer
