from rest_framework.permissions import BasePermission


class MyBasePermission(BasePermission):
    message = 'Su Perfil No tiene permiso para realizar esta acción'


class IsNotUserAS(MyBasePermission):
    def __init__(self, role_exclude, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_exclude = role_exclude

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role != self.role_exclude


class IsSchoolUser(MyBasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'school'


class IsSrudentlUser(MyBasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'student'


class IsTeacherUser(MyBasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'teacher'


class IsGuestUser(MyBasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'guest'
