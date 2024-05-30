from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# /dashboard-estudiante/
class DashboardStudentTV(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'dashboard-student.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)