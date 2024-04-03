import re

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from accounts.models import CustomUserModel
from django.core.files import File
from django.core.files.base import ContentFile


# /api/user/upload-picture/<int:pk>/<str:filename>/
class UploadPictureFileAPIView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, pk, filename, *args, **kwargs):
        file_obj = request.FILES['file']
        user = CustomUserModel.objects.get(pk=pk)
        if not re.search(r'\.(png|jpg|jpeg|gif|bmp|tiff|svg)$', filename, re.IGNORECASE):
            return Response({
                'message': 'Archivo no permitido',
                'status': 'error',
                'url': ''
            }, status=status.HTTP_400_BAD_REQUEST)
        user.picture.delete()
        filename = str(user.pk) + filename[filename.rfind('.'):]
        user.picture.save(filename, file_obj.file, save=True)
        return Response({
            'message': 'Archivo subido correctamente',
            'status': 'success',
            'url': user.picture.url
        }, status=status.HTTP_201_CREATED)