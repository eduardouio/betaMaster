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
