from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from accounts.models import CustomUserModel
from django.core.files import File


# /api/user/upload-cv/<int:pk>/<str:filename>/
class UploadCVFileView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, pk, filename, *args, **kwargs):
        file_obj = request.data['file']
        user = CustomUserModel.objects.get(pk=pk)
        django_file = File(file_obj.file)
        if not filename.endswith('.pdf'):
            return Response({
                'message': 'Archivo no permitido',
                'status': 'error',
                'url': ''
            }, status=status.HTTP_400_BAD_REQUEST)
        user.cv.delete()
        user.cv.save(str(user.pk) + '.pdf', django_file, save=True)
        return Response({
            'message': 'Archivo subido correctamente',
            'status': 'success',
            'url': user.cv.url
        }, status=status.HTTP_201_CREATED)
