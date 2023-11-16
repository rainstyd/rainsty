FROM arm64v8/python:3.6.8

MAINTAINER rainsty <rainstyd@sina.com>

WORKDIR /

RUN sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc \
	&& echo "deb http://mirrors.ustc.edu.cn/debian/ stretch main contrib non-free\n\
deb http://mirrors.ustc.edu.cn/debian/ stretch-backports main contrib non-free\n\
deb http://mirrors.ustc.edu.cn/debian/ stretch-proposed-updates main contrib non-free\n\
deb http://mirrors.ustc.edu.cn/debian/ stretch-updates main contrib non-free" > /etc/apt/sources.list \
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

ARG HTTPD_PROXY=http://127.0.0.1:8799/registry
ARG JDK_FILE=OpenJDK8U-jdk_aarch64_linux_hotspot_8u322b06.tar.gz
ARG JDK_HOME=jdk8u322-b06
ARG SPARK_FILE=spark-2.4.8-bin-hadoop2.7.tgz
ARG SPARK_HOME=spark-2.4.8-bin-hadoop2.7

RUN wget $HTTPD_PROXY/jdk/$JDK_FILE
RUN wget $HTTPD_PROXY/spark/$SPARK_FILE

RUN tar -xvf $JDK_FILE \
    && tar -xvf $SPARK_FILE

ENV JAVA_HOME /$JDK_HOME
ENV SPARK_HOME /$SPARK_HOME
ENV PATH $SPARK_HOME/bin:$JAVA_HOME/bin:$PATH

RUN echo "#!/bin/bash\n\
set -e\n\
/etc/init.d/ssh start -D &\n\
exec \"\$@\"" > /docker-entrypoint.sh \
    && chmod +x /docker-entrypoint.sh

EXPOSE 22 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/etc/init.d/ssh", "start", "-D"]

# docker build --build-arg HTTPD_PROXY=http://192.168.0.188:8799/registry -t alarm/spark:latest .
# docker tag alarm/spark:latest repo.tzt.cn:8088/alarm/spark:armv1_2.4.8-2.7
