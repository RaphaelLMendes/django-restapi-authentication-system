# syntax=docker/dockerfile:1

FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 80
EXPOSE 443

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]