FROM python:3.10-alpine3.19

COPY requirments.txt /temp/requirments.txt

COPY service /service
WORKDIR /service
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirments.txt

RUN adduser --disabled-password service-user

USER service-user