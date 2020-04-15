#!/bin/bash

function main(){
    pip install --upgrade pip
    cat /home/falconApp/requirements.txt|xargs pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    cd /home/falconApp
    nohup gunicorn -w 2 manage_app:app -b 0.0.0.0:5000 --timeout 1800 &
}

main
