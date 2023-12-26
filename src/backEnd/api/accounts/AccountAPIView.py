from accounts.models import CustomUserModel as UserModel
from api.serializers import UserSerializer
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.views import APIView


class listUsers(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer