from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .filters import TaskFilter
from .models import Task, TaskAssignment
from .serializers import TaskSerializer, UserRegistrationSerializer, TaskAssignmentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.select_related('task', 'user').all()
    serializer_class = TaskAssignmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task_assignment = serializer.save()

        user = task_assignment.user
        task = task_assignment.task

        if user.email:
            subject = f"You was assigned to the task: {task.title}!"
            message = f"""
                Hello, {user.username}!
                You was assigned as '{task_assignment.role}' for the task:
                    - Title: {task.title}
                    - Description: {task.description}
                    - Due date: {task.due_date}
                Congradulations!
                {task.author}!
            """

            send_mail(
                subject,
                message,
                None,
                [user.email],
                fail_silently=False
            )
