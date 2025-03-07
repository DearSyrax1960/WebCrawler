from django.contrib.auth.models import User
from rest_framework.test import APIClient

import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False, is_superuser=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff, is_superuser=is_superuser))

    return do_authenticate
