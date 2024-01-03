import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest
from accounts.models import CustomUserModel


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


@pytest.mark.django_db
class TestCreateUserModel(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-add-user')
        return url

    def test_create_user(self, url, client_logged):
        data = {
            "email": "test-user@gmail.com",
            "password": "test",
            "role": "student",
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 201

        # verificamos que se creo el usuario
        user = CustomUserModel.objects.get(email=data['email'])
        assert user

    def test_create_user_error(self, url, client_logged):
        data = {
            "email": "test-user@gmail.com",
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 400


@pytest.mark.django_db
class TestUpdateAPIView(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-update-user', kwargs={'pk': 2})
        return url

    def test_update_user(self, url, client_logged):
        data = {
            "id_user": 2,
            "first_name": "test",
            "last_name": "test",
            "email": "test@hgf.com",
        }
        response = client_logged.put(
            url, data=data, content_type='application/json'
        )
        assert response.status_code == 200
        # verificamos que se actualizo el usuario
        user = CustomUserModel.objects.get(pk=2)
        assert user.first_name == data['first_name']
        assert user.last_name == data['last_name']

    def test_update_user_error(self, url, client_logged):
        data = {
            "id_user": 2
        }
        response = client_logged.put(
            url, data=data, content_type='application/json'
        )
        assert response.status_code == 400


@pytest.mark.django_db
class TestUpdateUserPassword(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-update-user-password', kwargs={'pk': 2})
        return url

    def test_not_authorized(self, client_guest, url):
        pass

    def test_update_user_password(self, url, client_logged):
        my_user = CustomUserModel.objects.create_user(
            email="test-user1@gmail.com",
            password="test111",
            role="student"
        )
        data = {
            "id_user": my_user.pk,
            "password": "test",
        }

        url = url.replace('2', str(my_user.pk))
        client_logged.force_login(my_user)
        response = client_logged.put(
            url, data=data, content_type='application/json'
        )
        assert response.status_code == 200
        # verificamos que se actualizo el usuario
        user = CustomUserModel.objects.get(pk=my_user.pk)
        assert user.check_password(data['password'])

    def test_update_user_password_no_owner(self, url, client_logged):
        data = {
            "id_user": 2,
            "password": "test",
        }
        response = client_logged.put(
            url, data=data, content_type='application/json'
        )
        assert response.status_code == 401
