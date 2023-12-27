import pytest
from django.urls import reverse
from tests.api.BaseTest import BaseTest


@pytest.mark.django_db
class TestDetailStudyPlans(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-study-plan', kwargs={'pk': 1})
        return url

    def test_get_detailstudy(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert response['id_study_plan'] == 1
        # comprobamos el depth de usuario
        assert response['coordinator']
        # comprobamos el depth de detalles
        assert response['details']
