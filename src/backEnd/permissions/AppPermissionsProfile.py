from rest_framework.permissions import BasePermission


class MyBasePermission(BasePermission):
    message = 'Su Perfil No tiene permiso para realizar esta acción'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser:
            return True

        return self.check_role(request.user)

    def check_role(self, user):
        raise NotImplementedError('Not implemented en subclase')


class IsNotUserAS(MyBasePermission):
    def __init__(self, role_exclude, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_exclude = role_exclude

    def check_role(self, user):
        return user.role != self.role_exclude


class IsSchoolUser(MyBasePermission):
    def check_role(self, user):
        return user.role == 'school'


class IsSrudentlUser(MyBasePermission):
    def check_role(self, user):
        return user.role == 'student'


class IsTeacherUser(MyBasePermission):
    def check_role(self, user):
        return user.role == 'teacher'


class IsGuestUser(MyBasePermission):
    def check_role(self, user):
        return user.role == 'guest'
