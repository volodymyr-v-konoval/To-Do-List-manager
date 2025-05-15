# Welcome to the To-Do TasksManager!
TasksManager is an application developed with DRF (Django Rest Framework), allowing users to manage tasks and register for them. The platform supports a variety of fearures including user registration, authentication, tasks creation, and registration. User assignet to the task will receive an e-mail message about this. The app integrates with PostgreSQL, Redis, and Celery to manage tasks and send email notifications to users upon event registration. Main endpoints of the app are covered by tests. The app includes Swager, Redoc and schemas documentation. All requests writes logs to the a local file.


# Features
- **User Authentication**: Register, log in, log out, session authentication and JWT token authentication
- **Tasks**: Create, Update, Delete your tasks
- **Tasks Assignments**: Assign a user as a assignee for the task


## Technologies Used
- **Django** - main framework to build the app
- **DRF** - for building the REST API
- **PostgreSQL** - for data storage
- **drf-spectacular** - for API documentation (Swagger, ReDoc, schemas)
- **django-filter** - for filtering tasks
- **Celery** - for assincronous sending emails
- **djnagorestframework-simplejwt** - to authenticate users by JWT tokens

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [DockerHub](#dockerhub)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

##Requirements
Before you start, make sure you have installed:
- Python 3.10 or higher
- Poetry for dependency management
- Docker

## Installation
1. Clone the repository:
```bash
git clone https://github.com/volodymyr-v-konoval/To-Do-List-manager.git
```

2. Setup virtual environment:
```bash
poetry install
poetry shell
```

3. Create .env file in your root directory and fill it with necessary environment variables.
Use env_example file as example

!!! If you don't want to configure mail service, just uncomment "EMAIL_BACKEND"  line in settings.py, and comment other SMTP settings or includ any SMTP values to .env to avoid errors.

4. Run Docker Compose to build and run the app locally with all dependencies:
```bash
docker compose up --build
```

## DockerHub
You can also pull the prebuilt image with all dependencies from DockerHub:

```bash
docker pull konovalvolodymyr/todo-manager
```

[DockerHub page](https://hub.docker.com/repository/docker/konovalvolodymyr/todo-manager/general)


## Usage
Once the project is up and running, visit:
```
http://127.0.0.1:8000/api/v1/docs/
```

The first user with admin role is created during startup. Credentials are defined in `entrypoint.sh`:
```
SUPERUSER: admin
EMAIL: admin@example.com
PASSWORD: adminpass
```

## Contributing
1. Fork the repository
2. Create a new branch:
```bash
git checkout -b feature-name
```
3. Make your changes
4. Push your branch:
```bash
git push origin feature-name
```
5. Create a pull request

## Author
[@volodymyr-v-konoval](https://github.com/volodymyr-v-konoval)(volodymyr.v.konoval@gmail.com)

## License
Copyright © 2025

_This README was generated with ❤️_

