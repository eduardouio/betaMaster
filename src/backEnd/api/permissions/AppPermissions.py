from rest_framework.permissions import BasePermission

MESSAGE = 'No tiene permiso para realizar esta acción'


class isNotUserAS(BasePermission):
    message = MESSAGE

    def __init__(self, role_exclude, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_exclude = role_exclude

    def has_permission(self, request, view):
        return request.user.role != self.role_exclude


class IsSchoolUser(BasePermission):
    message = MESSAGE

    def has_permission(self, request, view):
        return request.user.role == 'school'


class IsSrudentlUser(BasePermission):
    message = MESSAGE

    def has_permission(self, request, view):
        return request.user.role == 'student'


class IsTeacherUser(BasePermission):
    message = MESSAGE

    def has_permission(self, request, view):
        return request.user.role == 'teacher'
