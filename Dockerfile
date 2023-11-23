FROM python:3.8-alpine

RUN mkdir /code
WORKDIR /code

RUN pip install pipenv
COPY Pipfile* /
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . /code/
