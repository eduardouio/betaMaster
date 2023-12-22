from rest_framework.permissions import BasePermission


class IsTeacherUser(BasePermission):
    message = 'El perfirl no tiene acceso a esta información'

    def has_permission(self, request, view):
        return request.user.role == 'teacher'
