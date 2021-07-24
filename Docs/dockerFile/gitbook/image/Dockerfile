FROM fellah/gitbook:latest

MAINTAINER rainsty <rainstyd@sina.com>

ADD run.sh /run.sh
ENV TZ Asia/Shanghai

RUN npm config set registry https://registry.npm.taobao.org && \
    chmod +x /run.sh && \
    sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc && \
    mkdir /gitbook

WORKDIR /gitbook
EXPOSE 4000

CMD ["/bin/bash", "/run.sh"]
