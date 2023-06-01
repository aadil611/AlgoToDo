FROM python:3.10-slim-buster

WORKDIR /AlgoToDo

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip3 install --root-user-action=ignore -r requirements.txt

COPY . .

