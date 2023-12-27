from api.studyPlans.GenericsDetailAPIViews import (
    DetailStudyPlanAPIView,
    DetailStudyPlanDetailAPIView,
    UserDataAPIView,
    ActiveCourseAPIView
)
from django.urls import path

app_name = 'api'

urlpatterns = [

    # datos de usuario
    path('user/<int:pk>/', UserDataAPIView.as_view(), name='api-user-data'),
    # cursos activos
    path('active-courses/<int:pk>/',
         ActiveCourseAPIView.as_view(), name='api-active-courses'),
    # planes de estudio
    path('study-plan/<int:pk>/',
         DetailStudyPlanAPIView.as_view(), name='api-study-plan'),
    path('study-plan-detail/<int:pk>/',
         DetailStudyPlanDetailAPIView.as_view(), name='api-detail-study-plan'),
]
