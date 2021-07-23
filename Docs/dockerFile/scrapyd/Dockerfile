FROM python:3.6.5

MAINTAINER rainsty

WORKDIR /

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
RUN echo 'deb http://mirrors.163.com/debian/ jessie main non-free contrib' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib' >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y unzip xvfb wget
RUN apt-get install -y libxss1 libappindicator1 libindicator7 libatk-bridge2.0-0 libatspi2.0-0
RUN apt-get install -y libgconf2-4 libnss3-1d libxss1 libcurl3 libappindicator3-1 libasound2
RUN apt-get install -y libgbm1 libgtk-3-0 libxtst6 xdg-utils fonts-liberation lsb-release

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get -f install
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get -f install
RUN wget -N http://npm.taobao.org/mirrors/chromedriver/2.46/chromedriver_linux64.zip
RUN unzip /chromedriver_linux64.zip
RUN chmod +x /chromedriver
RUN ln -s /chromedriver /usr/local/bin/chromedriver

RUN apt-get -y install vim
RUN apt-get -y install cron

RUN apt-get clean

ADD ./volumes/run.sh /
ADD ./volumes/requirements.txt /
ADD ./volumes/scrapyd.conf /etc/scrapyd/

RUN /bin/bash /run.sh

EXPOSE 6800

CMD ["scrapyd"]
