#!/bin/bash

function main(){
    pip3 install --upgrade pip
    cat /home/flaskApp/requirements.txt|xargs pip3 install -i http://mirrors.aliyun.com/pypi/simple/
    chmod +x /home/flaskApp/rainDB/bin rainDB-shell
    cd /home/flaskApp
    bash startApp.sh

}

main
