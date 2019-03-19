FROM python:3.4-alpine

COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p flask
WORKDIR /flask
