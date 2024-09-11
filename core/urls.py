from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import TaskViewSet

router = DefaultRouter()
router.register(r"Task", TaskViewSet, basename="Task")


urlpatterns = [
    path(r"core/", include(router.urls)),
]
