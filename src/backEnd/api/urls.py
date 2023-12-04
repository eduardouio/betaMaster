from django.urls import path
from api.accounts import listUsers

urlpatterns = [
    # cuentas de usuario
    path('users', listUsers.as_view(), name='api-users-list'),
]
