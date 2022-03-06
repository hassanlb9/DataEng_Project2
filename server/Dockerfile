FROM python:3.9

WORKDIR /server

ADD . /server

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "app.py"]