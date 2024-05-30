from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


# /home-rv/
class HomeRV(LoginRequiredMixin, RedirectView):
    login_url = '/accounts/login/'

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        pages = {
            'PROFESOR': '/dashboard-profesor/',
            'ESTUDIANTE': '/dashboard-estudiante/',
            'COLEGIO': '/accounts/logout',
            'guest': '/accounts/logout/'
        }
        return pages[user.role]
