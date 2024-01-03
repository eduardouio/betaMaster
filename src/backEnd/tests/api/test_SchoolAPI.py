import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest
from schools.models import School


@pytest.mark.django_db
class TestSchoolCreateAPIView(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-add-school')
        return url

    def test_create_school(self, client_logged, url):
        data = {
            "name": "Test",
            "address": "Test",
            "phone": "123456789",
            "id_owner": 2,
            "email": "gvc@d.com",
            "ami_code": "123456789",
            "state": "pichincha",
            "city": "quito",
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 201
        # comprobamos el registro en la base de datos
        school = School.objects.filter(
            name=data['name'],
            address=data['address']
        ).first()
        assert school is not None
        assert school.phone == data['phone']
        assert school.id_owner.pk == data['id_owner']
        assert school.address == data['address']
        assert school.email == data['email']
        assert school.ami_code == data['ami_code']

    def test_dont_logged_in_user(self, client_guest, url):
        data = {
            "name": "Test",
        }
        response = client_guest.post(url, data=data)
        assert response.status_code == 403

    def test_incomplete_data(self, url, client_logged):
        data = {
            "name": "Test",
        }
        response = client_logged.post(url, data=data)
        assert response.status_code == 400
