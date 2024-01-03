from rest_framework.generics import CreateAPIView

from api.serializers import (
    BankAccountSerializer,
    SchoolSerializer
)
from permissions.AppPermissionsProfile import IsNotUserAS
from accounts.models import BankAccount
from schools.models import School


class BaseCreateAPIView(CreateAPIView):
    permission_classes = [IsNotUserAS]

    def get_permissions(self):
        permissions = []
        for perm in self.permission_classes:
            if (perm.__name__ == 'IsNotUserAS'):
                permissions.append(perm(role_exclude='guest'))
            else:
                permissions.append(perm())

        return permissions


# /api/bank-account/add/ -> api-add-bank-account
class CarateBanckAccountAPIView(BaseCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsNotUserAS]


# /api/school/add/ -> api-add-school
class CreateSchoolAPIView(BaseCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsNotUserAS]
