FROM python:3.11-buster

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=invera_tasks.settings.local

# working directory \
WORKDIR /app
COPY . /app

COPY pyproject.toml /app

# Configure server
RUN set -ex \
    && pip install --upgrade pip

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev