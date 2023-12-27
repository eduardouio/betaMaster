import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import CustomUserModel as UserModel

@pytest.mark.django_db
class TestDetailStudyPlans:

    @pytest.fixture
    def client_student(self, client):
        self.user.role = 'teacher'
        self.user.save()
        client.force_login(self.user)
        return client

    @pytest.fixture
    def client_guest(self, client):
        self.user.role = 'guest'
        self.user.save()
        client.force_login(self.user)
        return client

    def setup_method(self):
        self.user = UserModel(
            username='test',
            email='test@example.com',
            password='<PASSWORD.123>',
        )

    def test_get_detailstudy(self, client_student):
        url = reverse('api:api-study-plan', kwargs={'pk': 1})
        response = client_student.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id_study_plan'] == 1

        # comprobamos el depth de usuario
        assert response['coordinator']

    def test_not_authorized(self, client_guest):
        message = 'Su Perfil No tiene permiso para realizar esta acción'
        url = reverse('api:api-study-plan', kwargs={'pk': 1})
        response = client_guest.get(url)
        assert response.status_code == 403
        response = response.json()
        assert response['detail'] == message

    def test_dont_logged_in_user(self):
        message = 'Las credenciales de autenticación no se proveyeron.'
        url = reverse('api:api-study-plan', kwargs={'pk': 1})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 403
        response = response.json()
        assert response['detail'] == message
