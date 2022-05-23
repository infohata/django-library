# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./project_intro ./project_intro
COPY ./requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app/project_intro
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
CMD ["gunicorn", "-b", "0.0.0.0:8000", "project_intro.wsgi"]
