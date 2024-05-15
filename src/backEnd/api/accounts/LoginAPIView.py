from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


# /accounts/api/login/
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Usuario autenticado'}, status=200)

        return Response({'message': 'Usuario no existe'}, status=401)
