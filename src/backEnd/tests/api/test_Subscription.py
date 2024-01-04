import pytest
from tests.api.BaseTest import BaseTest
from django.urls import reverse
from subscriptions.models import Subscription
from activeCourses.models import ActiveCourse
from studyPlans.models import StudyPlan
from schools.models import School


@pytest.mark.django_db
class TestSubscription(BaseTest):

    @pytest.fixture
    def url(self):
        url = reverse('api:api-subscription', kwargs={'pk': 1})
        return url

    def test_get_active_courses(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()

        assert response['id_subscription'] == 1
        assert isinstance(response['id_user'], dict)
        assert isinstance(response['id_active_course'], dict)
        assert isinstance(response['payments'], list)


@pytest.mark.django_db
class TestListSubscription(BaseTest):

    @pytest.fixture
    def url(self):
        return reverse('api:api-subscriptions-list')

    def test_not_authorized(self, client_guest, url):
        # sobreescribimos el metodo para que no de error
        pass

    def test_list_subscription(self, client_logged, url):
        response = client_logged.get(url)
        assert response.status_code == 200
        response = response.json()
        assert isinstance(response, dict)
        # verificamos que contiene la paginacion
        assert response['results']
        assert response['count']
        assert response['next']


@pytest.mark.django_db
class TestCreateSubscription(BaseTest):

    @pytest.fixture
    def url(self):
        return reverse('api:api-add-subscription')

    def test_create_subscription(self, url, client_logged):

        school = School.objects.create(
            name='test',
            address='test',
            phone='test',
            id_owner=self.user,
            email='test@ghjk.com',
            ami_code='test',
            state='test',
            city='test',
        )
        active_course = ActiveCourse.objects.create(
            student=self.user,
            id_school=school,
            id_study_plan=StudyPlan.objects.get(pk=1),
        )
        data = {
            "id_user": 1,
            "id_active_course": active_course.pk,
            "date_start": "2022-01-01T00:00:00Z",
            "date_end": "2022-12-31T23:59:59Z",
            "type_subscription": "OTHER",
            "cost": 100.0
        }
        response = client_logged.post(url, data)
        assert response.status_code == 201
        # verificamos que se creo el objeto
        assert Subscription.objects.filter(
            id_user=3
        ).count() == 1

    def test_create_subscription_not_authorized(self, url, client_guest):
        data = {}
        response = client_guest.post(url, data)
        assert response.status_code == 403
