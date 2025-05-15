from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Task, TaskAssignment


User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('__all__')
        read_only_fields = ('slug', 'author')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class TaskAssignmentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    task_title = serializers.CharField(source='task.title', read_only=True)

    class Meta:
        model = TaskAssignment
        fields = ['id', 'task', 'task_title', 'user', 'username', 'role', 'assigned_at']
        read_only_fields = ['assigned_at']
