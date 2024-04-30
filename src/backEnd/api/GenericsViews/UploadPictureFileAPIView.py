import re

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUserModel


# /api/user/upload-picture/<int:pk>/
class UploadPictureFileAPIView(APIView):

    def post(self, request, pk, *args, **kwargs):
        file_obj = request.FILES['file']
        user = CustomUserModel.objects.get(pk=pk)
        if not re.search(
            r'\.(png|jpg|jpeg|gif|bmp|tiff|svg)$', file_obj.name, re.IGNORECASE
        ):
            return Response({
                'message': 'Archivo no permitido',
                'status': 'error',
                'url': ''
            }, status=status.HTTP_400_BAD_REQUEST)
        user.picture.delete()
        filename = str(user.pk) + file_obj.name[file_obj.name.rfind('.'):]
        user.picture.save(filename, file_obj.file, save=True)
        return Response({
            'message': 'Archivo subido correctamente',
            'status': 'success',
            'url': user.picture.url
        }, status=status.HTTP_201_CREATED)

    def get(self, request, pk, *args, **kwargs):
        user = CustomUserModel.objects.get(pk=pk)
        if not user.picture:
            return Response({
                'message': 'El usuario no tiene imagen de perfil',
                'status': 'error',
                'url': None
            }, status=status.HTTP_200_OK)

        return Response({
            'message': 'El usuario no tiene imagen de perfil',
            'status': 'ok',
            'url': user.picture.url
        }, status=status.HTTP_200_OK)
