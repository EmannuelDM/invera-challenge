import pytest

from core.models import Task


@pytest.fixture
def load_case_3():
    hotel_palace = User.objects.create(name="Hotel Palace", base_price=10)
