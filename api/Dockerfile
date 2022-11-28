FROM python:3.6-buster

WORKDIR /app

RUN apt install wget

RUN apt-get update \
    && apt-get -yy install libmariadb-dev

RUN apt install libmariadb3 libmariadb-dev

RUN apt install gcc

RUN pip install flask

RUN pip install mariadb

RUN pip install bcrypt

COPY . .

CMD ["python", "api.py"]