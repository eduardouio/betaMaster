from django.urls import path
from accounts.views import LoginTV, HomeRV, LogoutRV

app_name = "accounts"
urlpatterns = [
    path('', HomeRV.as_view(), name='home'),
    path('login/', LoginTV.as_view(), name='login'),
    path('logout/', LogoutRV.as_view(), name='logout'),
]
