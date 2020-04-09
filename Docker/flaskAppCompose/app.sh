#!/bin/bash

function main(){
    # pip3 install --upgrade pip
    cat /home/flaskApp/requirements.txt|xargs pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    chmod +x /home/flaskApp/rainDB/bin/rainDB-shell
    touch /home/flaskApp/logs/rainLog.log
    cd /home/flaskApp
    python3 appManage.py 5000
}

main
