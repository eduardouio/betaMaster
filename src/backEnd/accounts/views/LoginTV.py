from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from accounts.models import CustomUserModel


# /accounts/login/
class LoginTV(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        page_data = {
            'title_page': 'Inicio Sesion',
            'module_name': 'Accounts',
            'message': '',
            'satus': 'not_logged_in',
        }
        if request.user.is_authenticated:
            page_data['status'] = 'logged_in'
            page_data['message'] = 'Ya has iniciado sesion'

            # redireccionamos a cada Dashboard
            if request.user.role == 'asistente':
                return HttpResponseRedirect('/mobile/dashboard/')
            else:
                return HttpResponseRedirect('/')

        context = self.get_context_data(**kwargs)

        return self.render_to_response({**context, **page_data})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'asistente':
                return HttpResponseRedirect('/mobile/dashboard/')
                return HttpResponseRedirect('/')

        return HttpResponseRedirect('/accounts/login/?show_error=true')