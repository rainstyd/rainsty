#!/bin/bash

check_ll=`cat /root/.bashrc |grep "^alias ll" | awk -F '=' '{print $1}'`
echo ${check_ll}

if ! [ -n "${check_ll}" ]; then
    sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc
    source /root/.bashrc
fi

pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
