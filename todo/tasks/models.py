from django.db import models


class Task(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'PN', 'Pending'
        IN_PROGRESS = 'PR', 'In progress'
        COMPLETED = 'CM', 'Completed'

    title = models.CharField(max_length=250, unique_for_date='due_date')
    description = models.TextField(blank=True)
    due_date = models.DateField()
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
