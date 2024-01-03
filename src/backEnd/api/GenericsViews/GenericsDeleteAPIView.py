from rest_framework.generics import DestroyAPIView
from permissions.AppPermissionsProfile import IsNotUserAS
from accounts.models import BankAccount
from api.serializers import BankAccountSerializer


class BasedDestroyAPIView(DestroyAPIView):
    permission_classes = [IsNotUserAS]

    def get_permissions(self):
        permissions = []
        for perm in self.permission_classes:
            if (perm.__name__ == 'IsNotUserAS'):
                permissions.append(perm(role_exclude='guest'))
            else:
                permissions.append(perm())

        return permissions


# /api/bank-account/delete/<pk:int>/ -> api-delete-bank-account
class DeleteBankAccountAPIView(BasedDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsNotUserAS]

