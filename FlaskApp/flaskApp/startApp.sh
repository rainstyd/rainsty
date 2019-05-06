#!/bin/bash
PORT=$1
if [ ! $PORT ];then
    PORT=8001
fi

processInfo="python/bin/python3 appManage.py $PORT"


function start(){
    if [ -e 'nohup.out' ];then
        date=`date +%Y%m%d%H%M%S`
        mv nohup.out ./logs/nohup.out.bak${date}
        unset date
    fi

    enterPrt=$"\n"
    echo ${processInfo}
    nohup ./${processInfo} &
    enterPrint=$(echo -e $enterPrt)
    echo $enterPrint
    unset enterPrt
    unset enterPrint
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
if [ $? -eq 0 ];then
    echo "App has started, please stop first!"
    exit 1
fi
start
verify
if [ ! $? -eq 0 ];then
    echo "App service startup failed!"
    exit 2
else
    echo "App service startup successful!"
fi
unset processInfo

