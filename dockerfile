# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /HomeInsuranceQuoteApp

COPY requirements.txt requirements.txt
COPY . .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN FLASK_ENV=development && export FLASK_APP=app

CMD flask run --host=0.0.0.0 --port=5000