FROM python:3.6-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install xz-utils
RUN apt-get -y install curl

RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash - &&\
   apt-get install -y nodejs

RUN npm install -g npm@9.6.6

RUN npm fund

RUN apt install wget

RUN apt-get update \
    && apt-get -yy install libmariadb-dev

RUN apt install libmariadb3 libmariadb-dev

RUN apt install gcc

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "api.py"]