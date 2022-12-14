FROM ubuntu:20.04

WORKDIR /code

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip python3 locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY djangoTest1 .

# RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
EXPOSE 8001
# ENTRYPOINT /bin/bash -c "cd /code && nohup python3 manage.py runserver 0.0.0.0:8001 &"
