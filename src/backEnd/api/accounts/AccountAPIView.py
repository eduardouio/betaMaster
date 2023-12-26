from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from accounts.models import CustomUserModel as UserModel
from api.serializers import UserSerializer


class listUsers(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer