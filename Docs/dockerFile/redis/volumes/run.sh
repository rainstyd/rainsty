#!/bin/bash

check_ll=`cat /root/.bashrc |grep "^alias ll" | awk -F '=' '{print $1}'`
echo ${check_ll}

if ! [ -n "${check_ll}" ]; then
    sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc
    source /root/.bashrc
fi

# port password 开启持久化
redis-server --port 6379 --requirepass 123456  --appendonly yes
