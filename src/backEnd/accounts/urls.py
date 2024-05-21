from django.urls import path
from accounts.views import LoginTV, LogoutRV

app_name = "accounts"
urlpatterns = [
    path('login/', LoginTV.as_view(), name='login'),
    path('logout/', LogoutRV.as_view(), name='logout'),
]
