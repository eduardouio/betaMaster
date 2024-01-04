import io
import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from tests.api.BaseTest import BaseTest

from accounts.models import PersonalReferences, CustomUserModel


@pytest.mark.django_db
class TestPersonalCreateReferences(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-add-personal-reference')
        return url

    def test_create_personal_references(self, url, client_logged):
        new_user = CustomUserModel.objects.create(
            email="test-user22@gmial.com",
            password="test-password",
            role="student",
        )
        file = io.BytesIO(b"test")
        file.name = 'test.pdf'
        document = SimpleUploadedFile(
            file.name, file.read()
        )
        data = {
            "id_user": new_user.pk,
            "type": "personal",
            "document": document,
            "enterprise": "Google",
            "name_contact": "Juan Perez",
            "phone_contact": "123456789",
            "email_contact": "test2@gmail.com",
            "relationship": "buddy",
        }
        response = client_logged.post(url, data, format='multipart')
        assert response.status_code == 201
        # verificamos el objeto creado
        assert PersonalReferences.objects.filter(
            id_user=new_user
        ).count() == 1

    def test_incomplete_data(self, url, client_logged):
        data = {
            "id_user": 1,
        }
        response = client_logged.post(url, data)
        assert response.status_code == 400

    def test_create_personal_references_not_authorized(self, url, client_guest):
        data = {}
        response = client_guest.post(url, data)
        assert response.status_code == 403


@pytest.mark.django_db
class TestDeletePersonalReferences(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-delete-personal-reference', kwargs={'pk': 1})
        return url

    def test_delete_personal_references(self, url, client_logged):
        response = client_logged.delete(url)
        assert response.status_code == 204
        # verificamos que se elimino
        assert PersonalReferences.objects.filter(
            id_reference=1
        ).count() == 0

    def test_delete_personal_references_not_authorized(self, url, client_guest):
        response = client_guest.delete(url)
        assert response.status_code == 403
