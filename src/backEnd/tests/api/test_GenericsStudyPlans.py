import pytest
from django.urls import reverse
from accounts.models import CustomUserModel as UserModel
from api.studyPlans.GenericsAPIViews import (
    DetailStudyPlanAPIView,
    DetailStudyPlanDetailAPIView
)


@pytest.mark.django_db
class TestDetailStudyPlans:

    @pytest.fixture
    def client(self, client):
        my_user = UserModel.objects.create(
            username='test',
            email='test@example.com',
            password='<PASSWORD.123>',
            role='guest'
        )
        client.force_login(my_user)
        return client

    def setup_method(self):
        pass

    def test_get_detailstudy(self, client):
        url = reverse('api:api-study-plan', kwargs={'pk': 1})
        response = client.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id_study_plan'] == 1

        # comprobamos el depth de usuario
        assert response['coordinator']

