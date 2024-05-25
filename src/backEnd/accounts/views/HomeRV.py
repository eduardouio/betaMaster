from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRV(LoginRequiredMixin, RedirectView):
    login_url = '/accounts/login/'

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        pages = {
            'PROFESOR': '/dashboard-profesor/',
            'ESTUDIANTE': '/dashboard-estudiante/',
            'COLEGIO': '/dashboard-colegio/',
        }
        return pages[user.role]
