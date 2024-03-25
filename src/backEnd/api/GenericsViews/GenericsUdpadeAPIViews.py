import json
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from permissions.AppPermissionsProfile import IsNotUserAS
from accounts.models import BankAccount, CustomUserModel, PersonalReferences
from rest_framework.parsers import MultiPartParser

from api.serializers import (
    BankAccountSerializer,
    SchoolSerializer,
    UserSerializerPrivate,
    PersonalReferencesSerializer,
    PaymentSerializer
)
from schools.models import School
from subscriptions.models import Payment


class BasedUpdateAPIView(RetrieveUpdateAPIView):
    pass
    # # permission_classes = [IsNotUserAS]

    #def get_permissions(self):
    #    permissions = []
    # #    for perm in self.permission_classes:
    #        if (perm.__name__ == 'IsNotUserAS'):
    #            permissions.append(perm(role_exclude='guest'))
    #        else:
    #            permissions.append(perm())
    #    return permissions


# /api/bank-account/<pk:int>/ -> api-update-bank-account
class UpdateBankAccountAPIView(BasedUpdateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    # permission_classes = [IsNotUserAS]


# /api/school/<pk:int>/ -> api-update-school
class UpdateSchoolAPIView(BasedUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [IsNotUserAS]


# /api/user/<pk:int>/ -> api-update-user
class UpdateUserAPIView(BasedUpdateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializerPrivate
    # permission_classes = [IsNotUserAS]


# /api/user/update-password/<pk:int>/ -> api-update-user-password
class UpdateUserPassword(APIView):

    def put(self, request, pk, *args, **kwargs):
        data = json.loads(request.data) 
        if not data.get('password'):
            return Response(status=400)

        # verificamos que el usuario sea el mismo
        # if request.user.pk != pk:
        #     return Response(
        #         data={'message': 'Error, no puedes actualizar este usuario'},
        #         status=401
        #     )

        user = CustomUserModel.objects.get(pk=pk)
        user.set_password(data['password'])
        user.save()
        return Response(data={'message': 'password actualizado'}, status=200)


# /api/personal-references/<pk:int>/ -> api-update-personal-reference
class UpdatePersonalRefAPIView(BasedUpdateAPIView):
    queryset = PersonalReferences.objects.all()
    serializer_class = PersonalReferencesSerializer
    # permission_classes = [IsNotUserAS]
    parser_classes = [MultiPartParser]


# /api/payment/<pk:int>/ -> api-update-payment
class UpdatePaymentAPIView(BasedUpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # permission_classes = [IsNotUserAS]
