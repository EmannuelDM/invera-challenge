import json

import pytest
from django.contrib.auth.models import User
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_task():
    url = reverse('core:Task-list')
    client = APIClient()
    user = User.objects.create_user(username="pepito", password="pepito_1")
    data = {
        "user_id": user.id,
        'title': 'terminar tests de CRUD de task',
        'description': "Faltan el read, update y delete de una task"}
    response = client.post(url, data=json.dumps(data), content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['title'] == data['title']
