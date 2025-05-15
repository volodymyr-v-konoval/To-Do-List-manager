FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV PYTHONPATH=/app/todo
ENV DJANGO_SETTINGS_MODULE=todo.settings

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . /app/

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
