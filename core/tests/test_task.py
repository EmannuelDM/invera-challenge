import json

import pytest
from django.contrib.auth.models import User
from django.urls.base import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_task(authenticated_client):
    url = reverse('core:Task-list')
    user = User.objects.create_user(username="pepito", password="pepito_1")
    data = {
        "user_id": user.id,
        'title': 'terminar tests de CRUD de task',
        'description': "Faltan el read, update y delete de una task",
        'done': False}
    response = authenticated_client.post(url, data=json.dumps(data), content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['title'] == data['title']


@pytest.mark.django_db
def test_read_task(authenticated_client, get_task):
    user, task = get_task
    url = reverse('core:Task-list')
    response = authenticated_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['count'] == 1
    assert response.json()['results'][0]['title'] == task.title


@pytest.mark.django_db
def test_check_task(authenticated_client, get_task):
    user, task = get_task
    assert task.done is False
    url = reverse(f"core:Task-detail", kwargs={"pk": task.id})
    payload = {'done': True}
    response = authenticated_client.patch(url, data=json.dumps(payload), content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['done'] is True


@pytest.mark.django_db
def test_delete_task(authenticated_client, get_task):
    user, task = get_task
    url = reverse(f"core:Task-detail", kwargs={"pk": task.id})

    # Delete Task
    response = authenticated_client.delete(url, content_type="application/json")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Check deletion
    response = authenticated_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_404_NOT_FOUND
