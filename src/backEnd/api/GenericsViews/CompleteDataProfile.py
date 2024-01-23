from rest_framework.views import APIView
from accounts.models import CustomUserModel
from rest_framework.response import Response
from api.serializers import CompleteDataForTeacherSerializer
from django.shortcuts import get_object_or_404


# /api/complete-data-teacher/<int:pk>/ -> api-complete-data-teacher
class CompleteDataTeacher(APIView):
    """return all active courses by user"""
    def get(self, request, pk):
        user = get_object_or_404(CustomUserModel, pk=pk)
        serializer = CompleteDataForTeacherSerializer(user)
        return Response(serializer.data)
