import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


@pytest.mark.django_db
class TestActiveCoursesByUser(BaseTest)
    
    @pytest.fixture
    def url(self):
        url = reverse('api:api-active-courses-by-user', kwargs={'pk': 1})
        return url

    def test_hola(url, client_logged):
        assert False