from api.GenericsViews.GenericsDetailAPIViews import (
    DetailStudyPlanAPIView,
    DetailStudyPlanDetailAPIView,
    DetailBankAccountAPIView,
    UserDataAPIView,
    ActiveCourseAPIView,
    SubscriptionAPIView,
    PaymentAPIView,
    SchoolAPIView,
)
from api.GenericsViews.GenericsListAPIView import (
    ListStudyPlanAPIView,
    ListUserByRoleAPIView,
    ListActiveCourseAPIView,
    ListSubscriptionAPIView,
    ListSchoolsAPIView,
)
from api.GenericsViews.GenericsCreateAPIViews import (
    CarateBanckAccountAPIView,
    CreateSchoolAPIView,
)
from api.GenericsViews.GenericsDeleteAPIView import (
    DeleteBankAccountAPIView,
    DeleteSchoolAPIView
)
from api.GenericsViews.GenericsUdpadeAPIViews import (
    UpdateBankAccountAPIView,
    UpdateSchoolAPIView
)
from django.urls import path

app_name = 'api'

urlpatterns = [
    # datos de usuario
    path('user/<int:pk>/', UserDataAPIView.as_view(), name='api-user-data'),
    path('users-by-role/<str:role_name>/',
         ListUserByRoleAPIView.as_view(), name='api-users-by-role-list'),
    # bancos de usuario
    path('bank-account/<int:pk>/', DetailBankAccountAPIView.as_view(),
         name='api-detail-bank-account'),
    path('bank-account/add/', CarateBanckAccountAPIView.as_view(),
         name='api-add-bank-account'),
    path('bank-account/delete/<int:pk>/',
         DeleteBankAccountAPIView.as_view(), name='api-delete-bank-account'),
    path('bank-account/update/<int:pk>/',
         UpdateBankAccountAPIView.as_view(), name='api-update-bank-account'),
    # cursos activos
    path('active-course/<int:pk>/',
         ActiveCourseAPIView.as_view(), name='api-active-course'),
    path('active-courses/', ListActiveCourseAPIView.as_view(),
         name='api-active-courses-list'),
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
    path('subscriptions/', ListSubscriptionAPIView.as_view(),
         name='api-subscriptions-list'),
    # pagos de suscripciones
    path('payments-subscription/<int:pk>/',
         PaymentAPIView.as_view(), name='api-payments-subscription'),
    # colegios
    path('school/<int:pk>/', SchoolAPIView.as_view(), name='api-school-detail'),
    path('school/add/', CreateSchoolAPIView.as_view(), name='api-add-school'),
    path('school/delete/<int:pk>/',
         DeleteSchoolAPIView.as_view(), name='api-delete-school'),
    path('schools/', ListSchoolsAPIView.as_view(), name='api-schools-list'),
    path('school/update/<int:pk>/',
         UpdateSchoolAPIView.as_view(), name='api-update-school'),
]
