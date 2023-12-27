import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


@pytest.mark.django_db
class TestDetailDetailStudyPlans(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-detail-study-plan', kwargs={'pk': 1})
        return url

    def test_get_detailstudy(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id_study_plan_detail'] == 1
        # comprobamos el depth al plan de estudio
        assert response['id_study_plan']
