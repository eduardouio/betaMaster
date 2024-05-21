from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRV(LoginRequiredMixin, RedirectView):
    login_url = '/accounts/login/'
    url = '/admin/'

    def get(self, request, *args, **kwargs):
        user = request.user
        import ipdb; ipdb.set_trace()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
