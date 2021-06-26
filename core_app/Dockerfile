FROM python:3.8.10-alpine3.13

WORKDIR /code

ENV FLASK_APP web_app.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask","run"]