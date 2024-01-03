import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


@pytest.mark.django_db
class TestAccountUser(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-user-data', kwargs={'pk': 2})
        return url

    def test_get_user(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id'] == 2
        # verificamos la listas de referencias y cuentas
        assert isinstance(response['references'], list)
        assert isinstance(response['accounts'], list)


@pytest.mark.django_db
class TestListStudyPlans(BaseTest):

    @pytest.fixture
    def url(self):
        return reverse('api:api-users-by-role-list', kwargs={'role_name': 'student'})

    def test_not_authorized(self, client_guest, url):
        # sobreescribimos el metodo para que no de error
        pass

    def test_list_users_students(self, client_logged, url):
        url = url.replace('role_name', 'student')
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        assert response['results'][0]['role'] == 'student'

    def test_list_users_school(self, client_logged, url):
        url = url.replace('student', 'school')
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        assert response['results'][0]['role'] == 'school'
        # verificamos que contiene la paginacion
        assert response['results']
        assert response['count']
        assert response['next']

    def test_list_users_teacher(self, client_logged, url):
        url = url.replace('student', 'teacher')
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        assert response['results'][0]['role'] == 'teacher'
        # verificamos que contiene la paginacion
        assert response['results']
        assert response['count']
        assert response['next']
