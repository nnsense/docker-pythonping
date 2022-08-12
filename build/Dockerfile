FROM python:3

COPY requirements.txt /app/requirements.txt

WORKDIR /app

ENV WP_HOSTNAME=scanme.nmap.org

RUN pip3 install -r /app/requirements.txt

