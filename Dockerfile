FROM python:3.6-alpine
MAINTAINER "Dell Team 7"

# Install python libraries
COPY requirements.txt /tmp
RUN python -m pip install -U pip
RUN python -m pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

ADD . /var/www
COPY prod_run.py /var/www
