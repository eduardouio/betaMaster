from django.urls import path
from api.studyPlans import DetailStudyPlanAPIView

app_name = 'api'

urlpatterns = [

    # planes de estudio
    path('study-plans/<int:pk>/', DetailStudyPlanAPIView.as_view(), name='api-study-plan'),
]
