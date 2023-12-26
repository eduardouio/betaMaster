from rest_framework.permissions import BasePermission


class isNotUserAS(BasePermission):
    message = 'El perfil no tiene acceso a esta informacion'

    def __init__(self, role_exclude, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_exclude = role_exclude

    def has_permission(self, request, view):
        return request.user.role != self.role_exclude
