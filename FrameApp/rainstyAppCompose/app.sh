#!/bin/bash

function main(){
    pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    cat /home/rainstyApp/requirements.txt|xargs pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    cd /home/rainstyApp && bash app_start.sh
}

main
