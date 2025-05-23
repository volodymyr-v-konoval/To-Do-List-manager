# Generated by Django 5.2.1 on 2025-05-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, unique_for_date="due_date")),
                ("description", models.TextField(blank=True)),
                ("due_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PN", "Pending"),
                            ("PR", "In progress"),
                            ("CM", "Completed"),
                        ],
                        default="PN",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
