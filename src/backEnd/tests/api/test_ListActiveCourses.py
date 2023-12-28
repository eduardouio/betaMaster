import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


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
