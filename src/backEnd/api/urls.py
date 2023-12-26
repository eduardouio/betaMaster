from django.urls import path
from api.accounts import listUsers
from api.studyPlans import DetailStudyPlansAPIView

urlpatterns = [
    # cuentas de usuario
    path('users', listUsers.as_view(), name='api-users-list'),
    # planes de estudio
    path('study-plans/<int:pk>/', DetailStudyPlansAPIView.as_view(), name='api-study-plans'),
]
