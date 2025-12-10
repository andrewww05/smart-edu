from django.contrib import admin
from .models import AcademicYear, Semester, WeekType, Group, Teacher, Subject, Schedule

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(WeekType)
class WeekTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_shortened_form')
    list_filter = ('is_shortened_form',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'group', 'teacher', 'day_of_week', 'time_start', 'week_type')
    list_filter = ('academic_year', 'semester', 'week_type', 'day_of_week', 'group', 'teacher')
