import pytest


@pytest.mark.django_db
class TestAccounts():
    def test_create_user(self):
        assert 1 == 2
