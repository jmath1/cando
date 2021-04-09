FROM python:3.9
WORKDIR /srv/
COPY ./requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt
