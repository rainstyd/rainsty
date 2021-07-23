FROM python:3.6.5

MAINTAINER rainsty

WORKDIR /

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
RUN echo 'deb http://mirrors.163.com/debian/ jessie main non-free contrib' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib' >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y unzip xvfb wget

RUN apt-get -y install vim
RUN apt-get -y install cron

RUN apt-get clean

ADD ./volumes/run.sh /
ADD ./volumes/requirements.txt /

RUN /bin/bash /run.sh

EXPOSE 8000

CMD ["gerapy", "runserver", "0.0.0.0:8000"]
