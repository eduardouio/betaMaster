from rest_framework.permissions import BasePermission


class IsSrudentlUser(BasePermission):
    message = 'El perfirl no tiene acceso a esta información'

    def has_permission(self, request, view):
        return request.user.role == 'student'
