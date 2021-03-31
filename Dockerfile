FROM python:3.9
WORKDIR /srv/
COPY . /srv/
RUN pip install -r requirements.txt
