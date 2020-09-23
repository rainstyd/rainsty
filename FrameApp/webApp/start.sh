#!/bin/bash

if [ -e 'nohup.out' ];then
    date=`date +%Y%m%d%H%M%S`
    mv nohup.out ./logs/nohup.out.bak${date}
    unset date
fi

nohup ./main/main.py 80 &
