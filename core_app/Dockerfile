FROM python:3.7.6-buster


WORKDIR /code

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask","run"]