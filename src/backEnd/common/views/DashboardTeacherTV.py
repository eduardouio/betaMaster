from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardTeacherTV(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard-teacher.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

