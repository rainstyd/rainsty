#!/bin/bash


function checkSelf() {
    CHECK_LL=`cat /root/.bashrc |grep "^alias ll" | awk -F '=' '{print $1}'`

    if [[ -z "$CHECK_LL" ]]; then
        sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc
        source /root/.bashrc
    fi
}


function envSelf() {
    if [[ -z "$REDIS_PORT" ]]; then
        export REDIS_PORT="6379"
    fi

    if [[ -z "$REDIS_PASSWORD" ]]; then
        export REDIS_PASSWORD="123456"
    fi

    if [[ -z "$REDIS_APPENDONLY" ]]; then
        export REDIS_APPENDONLY="yes"
    fi

    if [[ -z "$REDIS_SOMAXCONN" ]]; then
        export REDIS_SOMAXCONN="512"
    fi
}


function runSelf() {
    echo $REDIS_SOMAXCONN > /proc/sys/net/core/somaxconn
    redis-server --port $REDIS_PORT --requirepass $REDIS_PASSWORD  --appendonly $REDIS_APPENDONLY
}


function main() {
    checkSelf
    envSelf
    runSelf
}


main
