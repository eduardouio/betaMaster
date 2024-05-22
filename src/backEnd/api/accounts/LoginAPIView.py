from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


# /accounts/api/login/
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response(
                {'message': 'Usuario autenticado',  'status': 'success'},
                status=200
            )

        return Response(
            {
                'message':
                'Usuario no existe, intente registrase o verifque el correo'
            }, status=401
        )
