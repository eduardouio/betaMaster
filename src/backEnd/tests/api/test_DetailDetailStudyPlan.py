import pytest
from rest_framework.test import APIClient
from django.urls import reverse
import random
from accounts.models import CustomUserModel as UserModel


@pytest.mark.django_db
class TestDetailDetailStudyPlans:
    @pytest.fixture
    def client_logged(self, client):
        self.user.role = random.choice(['student', 'teacher', 'school'])
        self.user.save()
        client.force_login(self.user)
        return client

    @pytest.fixture
    def client_guest(self, client):
        self.user.role = 'guest'
        self.user.save()
        client.force_login(self.user)
        return client

    @pytest.fixture
    def url(self):
        url = reverse('api:api-detail-study-plan', kwargs={'pk': 1})
        return url

    def setup_method(self):
        self.user = UserModel(
            username='test',
            email='test@example.com',
            password='<PASSWORD>.123',
        )

    def test_get_detailstudy(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id_study_plan_detail'] == 1
        # comprobamos el depth al plan de estudio
        assert response['id_study_plan']

    def test_not_authorized(self, client_guest, url):
        message = 'Su Perfil No tiene permiso para realizar esta acción'
        response = client_guest.get(url)
        assert response.status_code == 403
        response = response.json()
        assert response['detail'] == message

    def test_dont_logged_in_user(self, url):
        message = 'Las credenciales de autenticación no se proveyeron.'
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 403
        response = response.json()
        assert response['detail'] == message
