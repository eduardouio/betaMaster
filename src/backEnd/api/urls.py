from api.GenericsViews.GenericsDetailAPIViews import (
    DetailStudyPlanAPIView,
    DetailStudyPlanDetailAPIView,
    UserDataAPIView,
    ActiveCourseAPIView,
    SubscriptionAPIView,
    PaymentAPIView,
)
from api.GenericsViews.GenericsListAPIView import (
    ListStudyPlanAPIView,
    ListUserByRoleAPIView
)

from django.urls import path

app_name = 'api'

urlpatterns = [

    # datos de usuario
    path('user/<int:pk>/', UserDataAPIView.as_view(), name='api-user-data'),
    path('users-by-role/<str:role_name>/',
         ListUserByRoleAPIView.as_view(), name='api-users-by-role-list'),
    # cursos activos
    path('active-course/<int:pk>/',
         ActiveCourseAPIView.as_view(), name='api-active-course'),

    # planes de estudio
    path('study-plans/', ListStudyPlanAPIView.as_view(),
         name='api-list-study-plans'),
    path('study-plan/<int:pk>/',
         DetailStudyPlanAPIView.as_view(), name='api-study-plan'),
    path('study-plan-detail/<int:pk>/',
         DetailStudyPlanDetailAPIView.as_view(), name='api-detail-study-plan'),

    # suscripciones
    path('subscription/<int:pk>/',
         SubscriptionAPIView.as_view(), name='api-subscription'),

    # pagos de suscripciones
    path('payments-subscription/<int:pk>/',
         PaymentAPIView.as_view(), name='api-payments-subscription'),
]
