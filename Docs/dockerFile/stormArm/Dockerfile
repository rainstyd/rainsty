FROM arm64v8/python:3.6.8

MAINTAINER rainsty <rainstyd@sina.com>

WORKDIR /

RUN sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc
ADD ./volumes/sources.list /etc/spt/
RUN apt-get update
RUN sh -c '/bin/echo -e "123456\n123456\n" | passwd root'
RUN apt-get autoremove -y openssh-client
RUN apt-get autoremove -y openssh-server
RUN apt-get install -y openssh-client
RUN apt-get install -y openssh-server
RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sh -c '/bin/echo -e "\n\n\n\n" | ssh-keygen -t rsa'
RUN cd /root/.ssh/ && cp id_rsa.pub authorized_keys
RUN apt-get -y install vim
RUN apt-get clean

ADD ./volumes/apache-storm-1.1.0.tar.gz /
ADD ./volumes/OpenJDK8U-jdk_aarch64_linux_hotspot_8u302b08.tar.gz /
ADD ./volumes/leiningen-2.9.1.tar.gz /
ENV STORM_HOME /apache-storm-1.1.0
ENV JAVA_HOME /jdk8u302-b08
ENV LEIN_ROOT /root/.lein
ENV PATH $LEIN_ROOT:$STORM_HOME/bin:$JAVA_HOME/bin:$PATH
RUN ln -s /leiningen-2.9.1 /root/.lein

RUN apt-get install gcc -y
RUN apt-get install g++ -y
RUN apt-get install make -y
RUN apt-get clean
ADD ./volumes/v1.6.0-ARM64-PRE10.tar.gz /
RUN cd /librdkafka-1.6.0-ARM64-PRE10 && ./configure && make && make install
RUN ln -s /usr/local/lib/librdkafka.so.1 /usr/lib/librdkafka.so.1

ADD ./volumes/docker-entrypoint.sh /
ADD ./volumes/requirements.txt /
RUN chmod +x /docker-entrypoint.sh
RUN mkdir /log && mkdir /pyenv
RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

EXPOSE 22 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/etc/init.d/ssh", "start", "-D"]


# docker build -t rainsty/storm:latest .
