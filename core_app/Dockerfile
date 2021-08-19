FROM python:3.8.10-alpine3.13

WORKDIR /code

ENV FLASK_APP web_app.py

ENV FLASK_RUN_HOST 0.0.0.0


RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask","run"]