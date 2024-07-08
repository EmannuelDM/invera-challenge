from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.filters import TaskFilter
from core.models import Task
from core.pagination import StandardResultsSetPagination
from core.serializers import TaskSerializer, TaskWriteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        action = self.action
        if action in ['create', 'update', 'partial_update']:
            return TaskWriteSerializer
        return TaskSerializer
