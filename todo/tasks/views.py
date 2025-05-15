from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import TaskFilter
from .models import Task, TaskAssignment
from .serializers import TaskSerializer, UserRegistrationSerializer, TaskAssignmentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.select_related('task', 'user').all()
    serializer_class = TaskAssignmentSerializer
    permission_classes = [IsAuthenticated]
