from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class ValidateStudentMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            return redirect(reverse_lazy('accounts:login'))

        if not request.user.role != 'ESTUDIANTE':
            return redirect(reverse_lazy('accounts:login'))

        return super().dispatch(request, *args, **kwargs)
