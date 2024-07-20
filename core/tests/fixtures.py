import pytest
from django.contrib.auth.models import User

from core.models import Task


@pytest.fixture
def get_task():
    user = User.objects.create_user(username="pepito", password="pepito_1")
    data = {
        "user_id": user.id,
        'title': 'terminar tests de CRUD de task',
        'description': "Faltan el read, update y delete de una task",
        'done': False}
    task = Task.objects.create(**data)
    return user, task
