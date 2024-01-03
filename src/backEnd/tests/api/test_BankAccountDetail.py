import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


@pytest.mark.django_db
class TestBankAccountAPIView(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-detail-bank-account', kwargs={'pk': 1})
        return url

    def test_get_bank_account(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id_bank'] == 1
