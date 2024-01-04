from rest_framework.generics import CreateAPIView

from api.serializers import (
    BankAccountSerializer,
    SchoolSerializer,
    UserSerializer,
    PersonalReferencesSerializer,
    SubscriptionSerializer
)
from permissions.AppPermissionsProfile import IsNotUserAS
from accounts.models import BankAccount, CustomUserModel, PersonalReferences
from schools.models import School
from subscriptions.models import Subscription


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


# /api/user/add/ -> api-add-user
class CreateUserAPIView(BaseCreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsNotUserAS]


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


# /api/personal-references/add/ -> api-add-personal-reference
class CreatePersonalRefAPIView(BaseCreateAPIView):
    queryset = PersonalReferences.objects.all()
    serializer_class = PersonalReferencesSerializer
    permission_classes = [IsNotUserAS]


# /api/subscription/add/ -> api-add-subscription
class CreateSubscriptionAPIView(BaseCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsNotUserAS]
