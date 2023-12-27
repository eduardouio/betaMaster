import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


@pytest.mark.django_db
class TestSubscriptionPayments(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-payments-subscription', kwargs={'pk': 1})
        return url

    def test_get_payment_subscriptiom(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()

        assert response['id_subscription'] == 1
        assert isinstance(response['id_user'], dict)
        assert isinstance(response['payments'], list)
