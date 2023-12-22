import pytest
from django.urls import reverse
from api.studyPlans import DetailStudyPlansAPIView
from accounts.models import CustomUserModel


@pytest.mark.django_db
class TestDetailStudyPlansAV:

    @pytest.fixture
    def client(self, client):
        my_user = CustomUserModel.objects.create(
            username='test',
            email='test@example.com',
            password='<PASSWORD.123>'
        )
        client.force_login(my_user)
        return client

    @pytest.fixture
    def url(self):
        return reverse('api:studyplans-detail', kwargs={'pk': 1})

    def test_get_detailstudy(self, client, url):
        pass
