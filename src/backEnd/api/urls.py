from django.urls import path
from api.studyPlans import DetailStudyPlanAPIView, DetailStudyPlanDetailAPIView

app_name = 'api'

urlpatterns = [

    # planes de estudio
    path('study-plan/<int:pk>/',
         DetailStudyPlanAPIView.as_view(), name='api-study-plan'),
    path('study-plan-detail/<int:pk>/',
         DetailStudyPlanDetailAPIView.as_view(), name='api-detail-study-plan'),
]
