FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install django
RUN pip install psycopg2
ADD . /code/
WORKDIR /code/
