FROM python:3.6-buster

WORKDIR /app

RUN apt install wget

RUN apt-get update \
    && apt-get -yy install libmariadb-dev

RUN apt install libmariadb3 libmariadb-dev

RUN apt install gcc

RUN pip install flask

RUN pip install pymysql==1.0.2

RUN pip3 install mariadb

RUN pip install bcrypt

COPY . .

EXPOSE 5000

CMD ["python", "api.py"]