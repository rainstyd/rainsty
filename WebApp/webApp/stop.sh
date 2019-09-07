#!/bin/bash
kill -9 `ps -ef | grep "main.py 80" | grep -v grep | awk '{print $2}' | xargs`
date=`date +%Y%m%d%H%M%S`
mv nohup.out ./logs/nohup.out.bak${date}
