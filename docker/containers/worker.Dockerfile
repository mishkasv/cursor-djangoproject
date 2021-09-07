FROM python:3.9-slim

RUN apt-get update && apt-get install -y gettext

ADD . /dealer

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /dealer/requirements/dev.txt

WORKDIR dealer/scr