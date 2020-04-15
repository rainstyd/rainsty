#!/bin/bash

function main(){
    # pip install --upgrade pip
    cat /home/flaskApp/requirements.txt|xargs pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    chmod +x /home/flaskApp/rainDB/bin/rainDB-shell
    cd /home/flaskApp
    touch /home/flaskApp/logs/rainLog.log
    python3 appManage.py 5000
}

main
