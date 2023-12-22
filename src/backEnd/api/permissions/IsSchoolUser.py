from rest_framework.permissions import BasePermission


class IsSchoolUser(BasePermission):
    message = 'El perfirl no tiene acceso a esta información'

    def has_permission(self, request, view):
        return request.user.role == 'school'
