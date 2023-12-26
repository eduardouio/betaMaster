from django.urls import path
from api.accounts import listUsers
from api.studyPlans import DetailStudyPlanAPIView

app_name = 'api'

urlpatterns = [
    # cuentas de usuario
    path('users', listUsers.as_view(), name='api-users-list'),
    # planes de estudio
    path('study-plans/<int:pk>/', DetailStudyPlanAPIView.as_view(), name='api-study-plan'),
]
