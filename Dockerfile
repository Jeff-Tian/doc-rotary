FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y libreoffice

ADD webapp /webapp
ADD fonts /usr/share/fonts/

WORKDIR /webapp

RUN pip3 install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --timeout 600 --bind 0.0.0.0:$PORT wsgi

