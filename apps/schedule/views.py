from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Schedule, AcademicYear, Semester, WeekType, Group, Teacher, Subject

def schedule_page(request):
    context = {
        'academic_years': AcademicYear.objects.all(),
        'semesters': Semester.objects.all(),
        'week_types': WeekType.objects.all(),
        'groups': Group.objects.all(),
        'teachers': Teacher.objects.all(),
    }
    return render(request, 'page/schedule/index.html', context)

@require_GET
def filter_schedule(request):
    academic_year_id = request.GET.get('academic_year')
    semester_id = request.GET.get('semester')
    week_type_id = request.GET.get('week_type')
    group_id = request.GET.get('group')
    teacher_id = request.GET.get('teacher')
    is_teacher_mode = request.GET.get('is_teacher_mode') == 'true'
    
    # Optional filters
    day_of_week = request.GET.get('day_of_week') # 0-6 or None
    
    queryset = Schedule.objects.select_related(
        'subject', 'group', 'teacher', 'academic_year', 'semester', 'week_type'
    ).all()

    if academic_year_id:
        queryset = queryset.filter(academic_year_id=academic_year_id)
    if semester_id:
        queryset = queryset.filter(semester_id=semester_id)
    if week_type_id:
        queryset = queryset.filter(week_type_id=week_type_id)
    if day_of_week is not None:
        queryset = queryset.filter(day_of_week=int(day_of_week))

    if is_teacher_mode:
        if teacher_id:
            queryset = queryset.filter(teacher_id=teacher_id)
    else:
        if group_id:
            queryset = queryset.filter(group_id=group_id)

    data = []
    for s in queryset:
        data.append({
            'id': str(s.id),
            'subject': s.subject.name,
            'type': s.subject.get_type_display(),
            'time_start': s.time_start.strftime('%H:%M'),
            'time_end': s.time_end.strftime('%H:%M'),
            'building': s.building,
            'room': s.room,
            'teacher': s.teacher.full_name,
            'group': s.group.name if s.group else '',
            'day': s.get_day_of_week_display(),
        })

    return JsonResponse({'schedule': data})
