from django.db import models
import uuid

class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, help_text="e.g. 2023-2024")

    def __str__(self):
        return self.name

class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, help_text="e.g. Fall, Spring")

    def __str__(self):
        return self.name

class WeekType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, help_text="e.g. Even, Odd")

    def __str__(self):
        return self.name

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    is_shortened_form = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Subject(models.Model):
    TYPE_CHOICES = [
        ('Lecture', 'Lecture'),
        ('Seminar', 'Seminar'),
        ('Lab', 'Laboratory'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Schedule(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    week_type = models.ForeignKey(WeekType, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    time_start = models.TimeField()
    time_end = models.TimeField()
    building = models.CharField(max_length=50, default="k.9")
    room = models.CharField(max_length=50)

    class Meta:
        ordering = ['day_of_week', 'time_start']

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.time_start} - {self.subject}"
