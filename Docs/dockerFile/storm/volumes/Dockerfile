FROM python:3.6.8

MAINTAINER rainsty <rainstyd@sina.com>

WORKDIR /

RUN sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc \
    && echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib\n\
deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib\n\
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib\n\
deb http://deb.debian.org/debian stretch main\n\
deb http://security.debian.org/debian-security stretch/updates main\n\
deb http://deb.debian.org/debian stretch-updates main" > /etc/apt/sources.list \
    && cat /etc/apt/sources.list \
    && apt-get update

RUN apt-get autoremove -y openssh-client \
        openssh-server \
    && apt-get install -y openssh-client \
        openssh-server \
        vim \
        gcc \
        g++ \
        make \
    && apt-get clean

RUN sh -c '/bin/echo -e "123456\n123456\n" | passwd root' \
    && sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/g" /etc/ssh/sshd_config \
    && sh -c '/bin/echo -e "\n\n\n\n" | ssh-keygen -t rsa' \
    && cd /root/.ssh/ && cp id_rsa.pub authorized_keys

RUN wget https://archive.apache.org/dist/storm/apache-storm-1.1.0/apache-storm-1.1.0.tar.gz \
    && wget https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/linux/OpenJDK8U-jdk_x64_linux_hotspot_8u302b08.tar.gz \
    && wget https://github.com/technomancy/leiningen/releases/download/2.9.6/leiningen-2.9.6-standalone.zip \
    && wget https://github.com/technomancy/leiningen/archive/refs/tags/2.9.6.tar.gz

RUN tar -xvf apache-storm-1.1.0.tar.gz \
    && ln -s /apache-storm-1.1.0/conf /conf \
    && tar -xvf OpenJDK8U-jdk_x64_linux_hotspot_8u302b08.tar.gz \
    && tar -xvf 2.9.6.tar.gz \
    && mkdir /root/.lein && mkdir /root/.lein/self-installs \
    && mv /leiningen-2.9.6-standalone.zip /root/.lein/self-installs/leiningen-2.9.6-standalone.jar \
    && mv /leiningen-2.9.6/bin/lein /root/.lein/ \
    && rm -rf apache-storm-1.1.0.tar.gz \
    && rm -rf OpenJDK8U-jdk_x64_linux_hotspot_8u302b08.tar.gz \
    && rm -rf 2.9.6.tar.gz && rm -rf leiningen-2.9.6

ENV STORM_HOME /apache-storm-1.1.0
ENV JAVA_HOME /jdk8u302-b08
ENV LEIN_ROOT /root/.lein
ENV PATH $LEIN_ROOT:$STORM_HOME/bin:$JAVA_HOME/bin:$PATH

RUN echo "#!/bin/bash\n\
set -e\n\
/etc/init.d/ssh start -D &\n\
exec \"\$@\"" > /docker-entrypoint.sh \
    && echo "streamparse==3.15.1\n\
redis==3.2.1\n\
pymysql==0.9.3\n\
confluent-kafka==1.6.0\n\
chardet==4.0.0" > requirements.txt \
    && chmod +x /docker-entrypoint.sh \
    && mkdir /log && mkdir /pyenv \
    && pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com \
    && pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

EXPOSE 22 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/etc/init.d/ssh", "start", "-D"]

# docker build -t rainsty/storm:latest .