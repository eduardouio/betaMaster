from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from api.serializers import (
    BankAccountSerializer,
    SchoolSerializer,
    UserSerializer,
    PersonalReferencesSerializer,
    SubscriptionSerializer,
    PaymentSubscriptionSerializer
)
from permissions.AppPermissionsProfile import IsNotUserAS
from accounts.models import BankAccount, CustomUserModel, PersonalReferences
from schools.models import School
from subscriptions.models import Subscription, Payment


class BaseCreateAPIView(CreateAPIView):
    pass
    # #permission_classes = [IsNotUserAS]
#
    #def get_permissions(self):
    #    permissions = []
    #    for perm in self.permission_classes:
    #        if (perm.__name__ == 'IsNotUserAS'):
    #            permissions.append(perm(role_exclude='guest'))
    #        else:
    #            permissions.append(perm())
#
    #    return permissions


# /api/user/add/ -> api-add-user
class CreateUserAPIView(CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        myUser = CustomUserModel.objects.create_user(
            email=request.data['email'],
            first_name=request.data['firstName'],
            last_name=request.data['lastName'],
            role=request.data['role'],
        )
        myUser.set_password(request.data['password'])
        myUser.save()
        return Response(
            {
                'id': myUser.pk,
                'email': myUser.email,
                'message': 'User created successfully.'
            }, status=status.HTTP_201_CREATED
        )


# /api/bank-account/add/ -> api-add-bank-account
class CarateBanckAccountAPIView(BaseCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    # permission_classes = [IsNotUserAS]


# /api/school/add/ -> api-add-school
class CreateSchoolAPIView(BaseCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [IsNotUserAS]


# /api/personal-references/add/ -> api-add-personal-reference
class CreatePersonalRefAPIView(BaseCreateAPIView):
    queryset = PersonalReferences.objects.all()
    serializer_class = PersonalReferencesSerializer
    # permission_classes = [IsNotUserAS]


# /api/subscription/add/ -> api-add-subscription
class CreateSubscriptionAPIView(BaseCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsNotUserAS]


# /api/payment/add/ -> api-add-payment
class CreatePaymentAPIView(BaseCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSubscriptionSerializer
    # permission_classes = [IsNotUserAS]