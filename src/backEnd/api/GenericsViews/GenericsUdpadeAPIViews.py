from rest_framework.generics import RetrieveUpdateAPIView
from permissions.AppPermissionsProfile import IsNotUserAS
from accounts.models import BankAccount
from api.serializers import (
    BankAccountSerializer,
    SchoolSerializer
)
from schools.models import School


class BasedUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsNotUserAS]

    def get_permissions(self):
        permissions = []
        for perm in self.permission_classes:
            if (perm.__name__ == 'IsNotUserAS'):
                permissions.append(perm(role_exclude='guest'))
            else:
                permissions.append(perm())

        return permissions


# /api/bank-account/<pk:int>/ -> api-update-bank-account
class UpdateBankAccountAPIView(BasedUpdateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsNotUserAS]


# /api/school/<pk:int>/ -> api-update-school
class UpdateSchoolAPIView(BasedUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsNotUserAS]