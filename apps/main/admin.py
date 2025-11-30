from django.contrib import admin
from .models import Group, Material, Room, Lesson, ActivityLog

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'year', 'created_at')
    search_fields = ('name', 'course')
    filter_horizontal = ('students',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'access_level', 'created_at')
    search_fields = ('title',)
    list_filter = ('access_level',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'created_at')
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('group', 'room', 'teacher', 'type', 'start', 'end')
    list_filter = ('type', 'start')
    search_fields = ('group__name', 'teacher__email')

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'target_type', 'ts')
    list_filter = ('action', 'target_type')
    search_fields = ('user__email', 'action')
