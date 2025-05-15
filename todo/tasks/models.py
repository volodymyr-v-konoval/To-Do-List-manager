from django.conf import settings
from django.db import models
from django.utils.text import slugify


class TaskAssignment(models.Model):
    ROLE_CHOICES = [
        ('leader', 'Team Leader'),
        ('dev', 'Developer'),
        ('qa', 'QA Engineer'),
    ]

    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('task', 'user')


class Task(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'PN', 'Pending'
        IN_PROGRESS = 'PR', 'In progress'
        COMPLETED = 'CM', 'Completed'

    title = models.CharField(max_length=250, unique_for_date='due_date')
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                related_name="tasks"
            )
    assignee = models.ManyToManyField(
                settings.AUTH_USER_MODEL,
                through='TaskAssignment',
                related_name='assigned_tasks'
            )
    description = models.TextField(blank=True)
    due_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.PENDING)
    

    class Meta:
        ordering = ['-due_date']
        indexes = [
            models.Index(fields=['-due_date']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
