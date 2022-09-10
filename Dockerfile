FROM ubuntu:20.04

WORKDIR /code

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip python3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY djangoTest1 .

# RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
EXPOSE 8001
ENTRYPOINT /bin/bash -c "cd /code && nohup python3 manage.py runserver 0.0.0.0:8001 &"
