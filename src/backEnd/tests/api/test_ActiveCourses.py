import pytest
from tests.api.BaseTest import BaseTest
from django.urls import reverse


@pytest.mark.django_db
class TestActiveCourses(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-active-courses', kwargs={'pk': 1})
        return url

    def test_get_active_courses(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()

        # compronamos el depth
        assert isinstance(response['id_school'], dict)
        assert isinstance(response['id_study_plan'], dict)
        assert isinstance(response['student'], dict)
        assert isinstance(response['teacher'], list)
