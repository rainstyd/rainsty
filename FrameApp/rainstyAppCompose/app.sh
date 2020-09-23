#!/bin/bash

function main(){
    pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com >> /dev/null
    cat /home/rainstyApp/requirements.txt|xargs pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com >> /dev/null
    cd /home/rainstyApp && bash app_start.sh
}

main
