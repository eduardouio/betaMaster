from rest_framework.views import APIView
from accounts.models import CustomUserModel
from rest_framework.response import Response
from api.serializers import (
    CompleteDataForTeacherSerializer,
    CompleteDataForStudentSerializer
)
from django.shortcuts import get_object_or_404


# /api/user/complete-data-teacher /{idUser}/ -> api-teacher-data
class TeacherDataApiView(APIView):
    """return all active courses by user"""

    def get(self, request, pk):
        user = get_object_or_404(CustomUserModel, pk=pk)
        if user.role != 'PROFESOR':
            return Response({'error': 'user is not a teacher'})

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


# /api/user/data-student-by-teacher/student/{idUser}/teacher/{idTeacher}/ -> api-student-data-teacher
class StudentDataForTeacherAPIView(APIView):

    def get(self, request, id_student, id_teacher):
        user = get_object_or_404(CustomUserModel, pk=id_student)
        if user.role != 'ESTUDIANTE':
            return Response({'error': 'user is not a student'})

        serializer = CompleteDataForStudentSerializer(user)
        data = []

        for active_course in serializer.data['active_courses']:
            if id_teacher in active_course['teacher']:
                row = {
                    'active_course': {
                        'id_active_courses': active_course['id_active_courses'],
                        'id_student': id_student,
                        'id_school': active_course['id_school'],
                        'id_teacher': active_course['teacher'],
                        'period': active_course['period'],
                        'state': active_course['state'],
                    },
                    'school': None,
                    'teachers': []
                }

                for school in serializer.data['school']:
                    if active_course['id_school'] == school['id']:
                        row['school'] = school

                for teacher in serializer.data['teachers']:
                    for teacher_active_course in active_course['teacher']:
                        if teacher_active_course == teacher['id']:
                            row['teachers'].append(teacher)

                data.append(row)

        report = {
            'student': serializer.data['student'],
            'active_courses': data
        }

        return Response(report)


# /api/user/complete-data-student/<int:pk>/ -> api-student-data
class StudentDataAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(CustomUserModel, pk=pk)
        if user.role != 'ESTUDIANTE':
            return Response({'error': 'user is not a student'})

        serializer = CompleteDataForStudentSerializer(user)
        data = []

        for active_course in serializer.data['active_courses']:
            row = {
                'active_course': {
                    'id_active_courses': active_course['id_active_courses'],
                    'id_student': pk,
                    'id_school': active_course['id_school'],
                    'id_teacher': active_course['teacher'],
                    'period': active_course['period'],
                    'state': active_course['state'],
                },
                'school': None,
                'teachers': []
            }

            for school in serializer.data['school']:
                if active_course['id_school'] == school['id']:
                    row['school'] = school

            for teacher in serializer.data['teachers']:
                for teacher_active_course in active_course['teacher']:
                    if teacher_active_course == teacher['id']:
                        row['teachers'].append(teacher)

            data.append(row)
        report = {
            'active_courses': data
        }

        return Response(report)
