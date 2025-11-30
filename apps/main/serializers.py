from rest_framework import serializers
from .models import Group, Material, Room, Lesson, ActivityLog
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'second_name']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    uploaded_by_details = UserSerializer(source='uploaded_by', read_only=True)

    class Meta:
        model = Material
        fields = '__all__'
        extra_kwargs = {'uploaded_by': {'read_only': True}}

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    group_details = GroupSerializer(source='group', read_only=True)
    room_details = RoomSerializer(source='room', read_only=True)
    teacher_details = UserSerializer(source='teacher', read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = ActivityLog
        fields = '__all__'
