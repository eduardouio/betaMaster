from rest_framework import serializers

from accounts.models import User, PersonalReferences
from activeCourses.models import ActiveCourse
from schools.models import School
from studyPlans.models import StudyPlan, StudyPlanDetail
from subscriptions.models import Subscription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class PersonalReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalReferences
        fields = ['__all__']


class ActiveCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveCourse
        fields = ['__all__']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['__all__']


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ['__all__']
        depth = 1


class studyPlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlanDetail
        fields = ['__all__']
        depth = 1


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['__all__']
        depth = 1
