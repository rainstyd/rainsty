FROM python:3.6.5

MAINTAINER rainsty <rainstyd@sina.com>

WORKDIR /

RUN sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
RUN echo 'deb http://mirrors.163.com/debian/ jessie main non-free contrib' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib' >> /etc/apt/sources.list

RUN apt-get update

RUN sh -c '/bin/echo -e "123456\n123456\n" | passwd root'
RUN apt-get autoremove -y openssh-client
RUN apt-get install -y openssh-server
RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sh -c '/bin/echo -e "\n\n\n\n" | ssh-keygen -t rsa'

RUN apt-get -y install vim

RUN apt-get clean

ADD ./volumes/apache-storm-1.1.0.tar.gz /
ADD ./volumes/jdk-8u231-linux-x64.tar.gz /

ENV STORM_HOME /apache-storm-1.1.0
ENV JAVA_HOME /jdk1.8.0_231
ENV LEIN_ROOT /root/.lein
ENV PATH $STORM_HOME/bin:$JAVA_HOME/bin:$PATH

ADD ./volumes/leiningen-2.9.1.tar.gz /
RUN mv /leiningen-2.9.1/lein /usr/local/bin/ && mv /leiningen-2.9.1 /root/.lein

ADD ./volumes/run.sh /
ADD ./volumes/requirements.txt /

RUN chmod +x /run.sh
RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
RUN mkdir /log && mkdir /pyenv

EXPOSE 22
EXPOSE 8000

ENTRYPOINT ["/run.sh"]
CMD ["/usr/sbin/sshd", "-D"]
