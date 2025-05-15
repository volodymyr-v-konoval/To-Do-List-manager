from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_assignment_email(user_email, username, task_title, task_description, due_date, role):
    subject = f"You were assigned to the task: {task_title}"
    message = f"""
                Hello, {username}!
                You was assigned as '{role}' for the task:
                    - Title: {task_title}
                    - Description: {task_description}
                    - Due date: {due_date}
                Congradulations!
                To-Do App!
            """

    send_mail(
        subject,
        message,
        None,
        [user_email]
    ) 
