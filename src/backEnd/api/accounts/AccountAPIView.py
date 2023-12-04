from resr_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class listUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer