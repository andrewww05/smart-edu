from .models import ActivityLog, Lesson, Material

class ActivityLogger:
    @staticmethod
    def log_action(user, action, target_type, target_id):
        ActivityLog.objects.create(
            user=user,
            action=action,
            target_type=target_type,
            target_id=target_id
        )

class ScheduleService:
    @staticmethod
    def get_schedule_for_group(group_id, start_date=None, end_date=None):
        queryset = Lesson.objects.filter(group_id=group_id)
        if start_date:
            queryset = queryset.filter(start__gte=start_date)
        if end_date:
            queryset = queryset.filter(end__lte=end_date)
        return queryset.order_by('start')

    @staticmethod
    def get_schedule_for_teacher(teacher_id, start_date=None, end_date=None):
        queryset = Lesson.objects.filter(teacher_id=teacher_id)
        if start_date:
            queryset = queryset.filter(start__gte=start_date)
        if end_date:
            queryset = queryset.filter(end__lte=end_date)
        return queryset.order_by('start')

class MaterialService:
    @staticmethod
    def upload_material(user, title, url, access_level):
        material = Material.objects.create(
            title=title,
            url=url,
            uploaded_by=user,
            access_level=access_level
        )
        ActivityLogger.log_action(user, 'upload_material', 'material', material.id)
        return material
