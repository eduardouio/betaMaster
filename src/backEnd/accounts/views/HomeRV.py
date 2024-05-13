from django.views.generic import TemplateView


# /accounts/home/
class HomeRV(TemplateView):
    template_name = 'accounts/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
