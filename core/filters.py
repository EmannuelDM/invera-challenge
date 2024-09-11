from datetime import datetime

from django_filters import rest_framework as filters
from django.db.models import QuerySet

from core.models import Task


class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    created_at = filters.DateFilter(field_name="created_at", lookup_expr="gte")

    class Meta:
        model = Task
        fields = []
