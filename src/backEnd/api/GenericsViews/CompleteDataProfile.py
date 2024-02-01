from rest_framework.views import APIView
from accounts.models import CustomUserModel
from rest_framework.response import Response
from api.serializers import CompleteDataForTeacherSerializer
from django.shortcuts import get_object_or_404


# /api/user/teacher-data/{idUser}/ -> api-teacher-data
class TeacherDataApiView(APIView):
    """return all active courses by user"""

    def get(self, request, pk):
        user = get_object_or_404(CustomUserModel, pk=pk)
        serializer = CompleteDataForTeacherSerializer(user)
        data = []

        for active_course in serializer.data['active_courses']:
            row = {
                'active_course': {
                    'id_active_courses': active_course['id_active_courses'],
                    'id_student': active_course['student'],
                    'id_school': active_course['id_school'],
                    'id_teacher': pk,
                    'period': active_course['period'],
                    'state': active_course['state'],
                },
                'school': None,
                'student': None,
            }

            for school in serializer.data['school']:
                if active_course['id_school'] == school['id']:
                    row['school'] = school

            for student in serializer.data['students']:
                if active_course['student'] == student['id']:
                    row['student'] = student

            data.append(row)

        return Response(data)
