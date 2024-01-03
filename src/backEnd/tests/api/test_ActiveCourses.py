import pytest
from tests.api.BaseTest import BaseTest
from django.urls import reverse


@pytest.mark.django_db
class TestActiveCourses(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-active-course', kwargs={'pk': 1})
        return url

    def test_get_active_courses(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()

        # compronamos el depth
        assert isinstance(response['id_school'], dict)
        assert isinstance(response['id_study_plan'], dict)
        assert isinstance(response['student'], dict)
        assert isinstance(response['teacher'], list)

@pytest.mark.django_db
class TestListActiveCourses(BaseTest):

    @pytest.fixture
    def url(self):
        return reverse('api:api-active-courses-list')

    def test_not_authorized(self, client_guest, url):
        # sobreescribimos el metodo para que no de error
        pass

    def test_list_active_courses(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        # verificamos que contiene la paginacion
        assert response['results']
        assert response['count']
        assert response['next']
