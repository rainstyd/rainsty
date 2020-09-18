#!/bin/bash


function checkSelf {
    check_ll=`cat /root/.bashrc |grep "^alias ll" | awk -F '=' '{print $1}'`

    if ! [ -n "${check_ll}" ]; then
        sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g" /root/.bashrc
        source /root/.bashrc
    fi
}


function envSelf {
    if [[ -z "$REDIS_PORT" ]]; then
        export $REDIS_PORT="6379"
    fi

    if [[ -z "$REDIS_PASSWORD" ]]; then
        export REDIS_PASSWORD="123456"
    fi

    if [[ -z "$REDIS_APPENDONLY" ]]; then
        export REDIS_APPENDONLY="yes"
    fi
}


function runSelf {
    redis-server --port $REDIS_PORT --requirepass $REDIS_PASSWORD  --appendonly $REDIS_APPENDONLY
}


function main {
    checkSelf
    envSelf
    runSelf
}


main
