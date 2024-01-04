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


@pytest.mark.django_db
class TestPaymentCreate(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-add-payment')
        return url

    def test_create_payment(self, client_logged, url):
        data = {
            'id_subscription': 1,
            'id_bank': 1,
            'payment_amount': 10000,
            'payment_date': '2021-01-01',
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 201
        response = response.json()

        assert response['id_subscription'] == data['id_subscription']
        assert response['id_bank'] == data['id_bank']
        assert response['payment_amount'] == data['payment_amount']
