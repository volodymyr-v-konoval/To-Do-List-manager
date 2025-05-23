from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from .models import Task


User = get_user_model()


class TaskAPITestCase(APITestCase):
    def setUp(self):
        super().setUp()

        Task.objects.all().delete()

        self.user = User.objects.create_user(username="testuser", password="testpass")
        response = self.client.post(reverse("token_obtain_pair"), {
                "username": "testuser",
                "password": "testpass"
            }
        )
        self.access_token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_register_user(self):
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "email": "new@example.com",
            "password": "newpass123"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task(self):
        response = self.client.post("/api/v1/tasks/", {
            "title": "Test Task",
            "description": "Just a test",
            "due_date": "2025-06-01",
            "status": "PN"
            }
        )
        print("RESPONSE:", response.status_code, response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_filter_tasks_by_status(self):
        Task.objects.create(
            title="Task1", due_date="2025-06-01", status="CM", author=self.user
        )
        Task.objects.create(
            title="Task2", due_date="2025-06-02", status="PN", author=self.user
        )

        response = self.client.get("/api/v1/tasks/?status=PN")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        tasks = response.data.get("results", response.data)
        filtered = [task for task in tasks if task["status"] == "PN" and task["author"] == self.user.id]
    
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['status'], 'PN')
