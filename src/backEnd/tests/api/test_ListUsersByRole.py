import pytest
from tests.api.BaseTest import BaseTest
from django.urls import reverse


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

    def test_list_users_teacher(self, client_logged, url):
        url = url.replace('student', 'teacher')
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        assert response['results'][0]['role'] == 'teacher'
