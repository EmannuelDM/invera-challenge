import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


def create_user_admin():
    admin, _ = User.objects.get_or_create(
        username="admin",
        email="admin@challenge.com.ar",
        is_staff=True,
        is_active=True,
        is_superuser=True)
    admin.set_password("admin_123")
    return admin


@pytest.fixture
def authenticated_client():
    user = create_user_admin()
    client = APIClient()
    client.force_authenticate(user=user)
    return client
