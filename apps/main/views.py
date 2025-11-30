from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Group, Material, Room, Lesson, ActivityLog
from .serializers import (
    GroupSerializer, MaterialSerializer, RoomSerializer, 
    LessonSerializer, ActivityLogSerializer
)
from .services import ScheduleService, MaterialService

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Use service to handle creation and logging
        MaterialService.upload_material(
            user=self.request.user,
            title=serializer.validated_data['title'],
            url=serializer.validated_data['url'],
            access_level=serializer.validated_data.get('access_level', 'public')
        )

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def my_schedule(self, request):
        # Example custom action using service
        if hasattr(request.user, 'student_groups') and request.user.student_groups.exists():
            # Assuming user can be in multiple groups, just taking first for simplicity or union
            # For now, let's just get lessons for the first group found
            group = request.user.student_groups.first()
            if group:
                lessons = ScheduleService.get_schedule_for_group(group.id)
                serializer = self.get_serializer(lessons, many=True)
                return Response(serializer.data)
        
        # If teacher
        lessons = ScheduleService.get_schedule_for_teacher(request.user.id)
        serializer = self.get_serializer(lessons, many=True)
        return Response(serializer.data)

class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]
