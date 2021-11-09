FROM python:3.9

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root --no-dev