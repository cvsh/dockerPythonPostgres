# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ADMIN_PASSWORD=password
ENV ADMIN_USER=admin
ENV ADMIN_EMAIL=admin@mail.com
WORKDIR /bcode
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY manage.py .
COPY . .