from rest_framework import serializers

from accounts.models import PersonalReferences, BankAccount, CustomUserModel
from activeCourses.models import ActiveCourse
from schools.models import School
from studyPlans.models import StudyPlan, StudyPlanDetail
from subscriptions.models import Subscription, Payment


class UserSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = [
            'password',
            'last_login',
            'token',
            'is_staff',
            'is_superuser',
            'username',
            'is_aproved',
            'is_confirmed_mail',
            'date_aproved',
            'notes',
            'user_permissions',
            'groups'
        ]


class PersonalReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalReferences
        fields = '__all__'


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'


class UserSerializerPrivate(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = [
            'password',
            'username',
        ]

    def to_representation(self, obj):
        data = super().to_representation(obj)
        references = PersonalReferences.objects.filter(id_user=obj)
        data['references'] = PersonalReferencesSerializer(
            references, many=True).data
        accounts = BankAccount.objects.filter(id_user=obj)
        data['accounts'] = BankAccountSerializer(accounts, many=True).data
        return data


class ActiveCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveCourse
        fields = '__all__'
        depth = 1

    def to_representation(self, obj):
        data = super().to_representation(obj)
        student = UserSerializerPublic(obj.student).data
        data['student'] = student
        teachers = UserSerializerPublic(obj.teacher.all(), many=True).data
        data['teacher'] = teachers
        return data


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class studyPlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlanDetail
        fields = '__all__'


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'

    def to_representation(self, obj):
        data = super().to_representation(obj)
        coordinator = UserSerializerPublic(obj.coordinator).data
        data['coordinator'] = coordinator
        details = StudyPlanDetail.objects.filter(id_study_plan=obj)
        data['details'] = studyPlanDetailSerializer(details, many=True).data
        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, obj):
        data = super().to_representation(obj)
        bank = BankAccount.objects.get(pk=obj.id_bank.pk)
        data['id_bank'] = BankAccountSerializer(bank).data
        return data


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        depth = 1

    def to_representation(self, obj):
        # sobreescribimos el usuario
        data = super().to_representation(obj)
        student = UserSerializerPublic(obj.id_user).data
        data['id_user'] = student

        # incluimos pagos
        payments = Payment.objects.filter(id_subscription=obj)
        data['payments'] = PaymentSerializer(payments, many=True).data

        return data


class PaymentSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

    def to_representation(self, obj):
        # sobreescribimos el usuario
        data = super().to_representation(obj)
        student = UserSerializerPublic(obj.id_user).data
        data['id_user'] = student

        # incluimos pagos
        payments = Payment.objects.filter(id_subscription=obj)
        data['payments'] = PaymentSerializer(payments, many=True).data

        return data
