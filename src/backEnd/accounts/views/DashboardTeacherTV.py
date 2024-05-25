from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# /dashboard-profesor/
class DashboardTeacherTV(TemplateView):
    template_name = 'dashboard-teacher.html'

    def get(self, request, *args, **kwargs):
        page_data = {
            'title_page': 'Dashboard Profesor',
            'module_name': 'Dashboard',
            'message': '',
            'status': 'not_logged_in',
        }
        context = self.get_context_data(**kwargs)
        return self.render_to_response({**context, **page_data})
