from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Task
from core.utils import get_logger
from user.serializers import UserModelSerializer

logger = get_logger(__name__)


class TaskSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'done', 'created_at']


class TaskWriteSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)

    class Meta:
        model = Task
        fields = ['user_id', 'title', 'description', 'done']

    def create(self, data):
        user_id = data.pop('user_id')
        user = User.objects.get(id=user_id)
        task = Task.objects.create(user=user, **data)
        logger.info(f"Task created: {task.title}")
        return task
