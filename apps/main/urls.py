from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GroupViewSet, MaterialViewSet, RoomViewSet, 
    LessonViewSet, ActivityLogViewSet
)

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'activity-logs', ActivityLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
