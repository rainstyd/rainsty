#!/bin/bash
PORT=$1
if [ ! $PORT ];then
    PORT=8001
fi
processInfo="python/bin/python3 appManage.py $PORT"


function stop(){
    kill -9 `ps -ef | grep "${processInfo}" | grep -v grep | awk '{print $2}' | xargs` >>/dev/null 2>&1
    date=`date +%Y%m%d%H%M%S`
    mv nohup.out ./logs/nohup.out.bak${date} >>/dev/null 2>&1
    unset date
    }

function verify(){
    process=`ps -ef | grep "${processInfo}" | grep -v grep`
    if [[ -z $process ]];then
        return 1
    else
        return 0
    fi
    }

verify
if [ $? -eq 1 ];then
    echo "App service does not exist, no need to stop!"
    exit 0
fi
stop
verify
if [ $? -eq 1 ];then
    echo "App service stop successful!"
fi
unset processInfo

