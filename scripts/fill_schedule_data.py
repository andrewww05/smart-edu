import os
import django
import sys
from datetime import time

# Setup Django environment
sys.path.append('/home/study/Desktop/smart-edu')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartedu.settings')
django.setup()

from apps.schedule.models import AcademicYear, Semester, WeekType, Group, Teacher, Subject, Schedule

def create_initial_data():
    # Clear existing data
    Schedule.objects.all().delete()
    Subject.objects.all().delete()
    Teacher.objects.all().delete()
    Group.objects.all().delete()
    WeekType.objects.all().delete()
    Semester.objects.all().delete()
    AcademicYear.objects.all().delete()

    # Academic Year
    year = AcademicYear.objects.create(name="2024-2025")
    
    # Semesters
    sem_fall = Semester.objects.create(name="Осінній")
    sem_spring = Semester.objects.create(name="Весняний")

    # Week Types
    week_odd = WeekType.objects.create(name="Непарний")
    week_even = WeekType.objects.create(name="Парний")

    # Groups
    group_301 = Group.objects.create(name="301", is_shortened_form=False)
    group_302 = Group.objects.create(name="302", is_shortened_form=True)

    # Teachers
    teacher_ivanov = Teacher.objects.create(full_name="Іванов І.І.")
    teacher_petrov = Teacher.objects.create(full_name="Петров П.П.")

    # Subjects
    sub_math = Subject.objects.create(name="Вища математика", type="Lecture")
    sub_physics = Subject.objects.create(name="Фізика", type="Lab")
    sub_history = Subject.objects.create(name="Історія", type="Seminar")

    # Schedule
    # Monday
    Schedule.objects.create(
        academic_year=year, semester=sem_fall, week_type=week_odd, group=group_301, teacher=teacher_ivanov, subject=sub_math,
        day_of_week=0, time_start=time(8, 30), time_end=time(10, 0), building="k.1", room="101"
    )
    Schedule.objects.create(
        academic_year=year, semester=sem_fall, week_type=week_odd, group=group_301, teacher=teacher_petrov, subject=sub_physics,
        day_of_week=0, time_start=time(10, 15), time_end=time(11, 45), building="k.1", room="205"
    )

    # Tuesday
    Schedule.objects.create(
        academic_year=year, semester=sem_fall, week_type=week_even, group=group_301, teacher=teacher_petrov, subject=sub_history,
        day_of_week=1, time_start=time(12, 0), time_end=time(13, 30), building="k.5", room="303"
    )

    print("Sample data created successfully!")

if __name__ == '__main__':
    create_initial_data()
