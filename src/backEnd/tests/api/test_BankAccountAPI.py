import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest
from accounts.models import BankAccount


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


@pytest.mark.django_db
class TestCreateBankAccountAPIView(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-add-bank-account')
        return url

    def test_create_bank_account(self, client_logged, url):
        data = {
            "id_user": 2,
            "nro_account": "123456789",
            "bank_name": "Banco de prueba",
            "type_account": "AHORROS",
            "email_notify": 'test@gm.com',
            "owner_name": "Test",
            "owner_dni": "123456789"
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 201

        # comprobamos el registro en la base de datos
        account = BankAccount.objects.filter(
            nro_account=data['nro_account'],
            email_notify=data['email_notify']
        ).first()

        assert account is not None
        assert account.bank_name == data['bank_name']
        assert account.type_account == data['type_account']
        assert account.owner_name == data['owner_name']
        assert account.owner_dni == data['owner_dni']

    def test_create_uncomplete_bank_account(self, client_logged, url):
        data = {
            "bank_name": "Banco de prueba",
            "type_account": "AHORROS",
            "owner_name": "Test",
            "owner_dni": "123456789"
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 400
        response = response.json()
        assert response['email_notify'][0] == 'Este campo es requerido.'
        assert response['nro_account'][0] == 'Este campo es requerido.'

    def test_not_authorized(self, client_guest, url):
        data = {
            "id_user": 2,
        }
        response = client_guest.post(url, data=data)
        assert response.status_code == 403


@pytest.mark.django_db
class TestDestroyAPIView(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-delete-bank-account', kwargs={'pk': 1})
        return url

    def test_delete_bank_account(self, client_logged, url):
        response = client_logged.delete(url)
        assert response.status_code == 204

        # comprobamos el registro en la base de datos
        account = BankAccount.objects.filter(id_bank=1).first()
        assert account is None

    def test_not_authorized(self, client_guest, url):
        response = client_guest.delete(url)
        assert response.status_code == 403
