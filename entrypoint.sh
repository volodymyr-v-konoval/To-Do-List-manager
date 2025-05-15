#!/bin/bash

echo "Applying migrations..."
python todo/manage.py makemigrations --noinput
python todo/manage.py migrate --noinput

echo "Creating an admin user..."

python todo/manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print("Superuser created.")
else:
    print("Superuser already exists.")
EOF

echo "Launching the Django-server..."
exec "$@"
