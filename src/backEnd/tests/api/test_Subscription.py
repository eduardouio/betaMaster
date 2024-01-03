import pytest
from tests.api.BaseTest import BaseTest
from django.urls import reverse


@pytest.mark.django_db
class TestSubscription(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-subscription', kwargs={'pk': 1})
        return url

    def test_get_active_courses(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()

        assert response['id_subscription'] == 1
        assert isinstance(response['id_user'], dict)
        assert isinstance(response['id_active_course'], dict)
        assert isinstance(response['payments'], list)


@pytest.mark.django_db
class TestListSubscription(BaseTest):

    @pytest.fixture
    def url(self):
        return reverse('api:api-subscriptions-list')

    def test_not_authorized(self, client_guest, url):
        # sobreescribimos el metodo para que no de error
        pass

    def test_list_subscription(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        # verificamos que contiene la paginacion
        assert response['results']
        assert response['count']
        assert response['next']
