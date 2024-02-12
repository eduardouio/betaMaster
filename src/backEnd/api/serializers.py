from rest_framework import serializers

from accounts.models import PersonalReferences, BankAccount, CustomUserModel
from activeCourses.models import ActiveCourse
from schools.models import School
from studyPlans.models import StudyPlan, StudyPlanDetail
from subscriptions.models import Subscription, Payment


class CompleteDataForTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = ['password']

    def to_representation(self, obj):
        data = {}
        active_courses = ActiveCourse.objects.filter(teacher=obj)
        data['active_courses'] = ActiveCourseSerializer(
            active_courses, many=True).data
        data['school'] = []
        data['students'] = []

        for active_course in active_courses:
            url = ''
            if active_course.student.picture:
                url = active_course.student.picture.url

            data['students'].append(
                {
                    'id': active_course.student.pk,
                    'picture': url,
                    'first_name': active_course.student.first_name,
                    'last_name': active_course.student.last_name,
                    'email': active_course.student.email,
                    'state': active_course.student.state,
                    'city': active_course.student.city,
                    'geolocation': active_course.student.geolocation,
                    'id_shool': active_course.id_school.pk,
                }
            )
            data['school'].append({
                'id': active_course.id_school.pk,
                'name': active_course.id_school.name,
                'email': active_course.id_school.email,
                'ami_code': active_course.id_school.ami_code,
                'state': active_course.id_school.state,
                'website': active_course.id_school.website,
                'logo': active_course.id_school.logo.url if active_course.id_school.logo else '',
                'phone': active_course.id_school.phone,
                'name_contact': active_course.id_school.name_contact,
                'city': active_course.id_school.city,
                'url_facebook': active_course.id_school.url_facebook,
                'url_instagram': active_course.id_school.url_instagram,
                'url_linkedin': active_course.id_school.url_linkedin,
                'address': active_course.id_school.address,
                'geolocation': active_course.id_school.geolocation,

            })

        return data


class CompleteDataForStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = ['password']

    def to_representation(self, obj):
        data = {}
        active_courses = ActiveCourse.objects.filter(student=obj)
        data['student'] = UserSerializerPublic(obj).data
        data['active_courses'] = ActiveCourseSerializer(
            active_courses, many=True).data
        data['school'] = []
        data['teachers'] = []

        for active_course in active_courses:

            for teacher in active_course.teacher.all():
                url = ''
                if teacher.picture:
                    url = teacher.picture.url

                if not any(teacher.pk == t['id'] for t in data['teachers']):
                    data['teachers'].append(
                        {
                            'id': teacher.pk,
                            'picture': url,
                            'first_name': teacher.first_name,
                            'last_name': teacher.last_name,
                            'email': teacher.email,
                            'state': teacher.state,
                            'city': teacher.city,
                            'geolocation': teacher.geolocation,
                        }
                    )

            data['school'].append({
                'id': active_course.id_school.pk,
                'name': active_course.id_school.name,
                'email': active_course.id_school.email,
                'ami_code': active_course.id_school.ami_code,
                'state': active_course.id_school.state,
                'city': active_course.id_school.city,
                'address': active_course.id_school.address,
                'geolocation': active_course.id_school.geolocation,

            })

        return data


class CompleteDataForSchool(serializers.ModelSerializer):
    pass


class UserSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = [
            'password',
            'last_login',
            'token',
            'is_staff',
            'is_superuser',
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'


class UserSerializerPrivate(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = [
            'password',
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


class ActiveCourseSerializerComplete(serializers.ModelSerializer):
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


class SubscriptionSerializerComplete(serializers.ModelSerializer):
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
        model = Payment
        fields = '__all__'
