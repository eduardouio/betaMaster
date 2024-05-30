from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# /dashboard-profesor/
class DashboardTeacherTV(TemplateView):
    template_name = 'dashboard-teacher.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
