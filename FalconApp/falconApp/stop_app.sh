#!/bin/bash

cat ./nohup.out |grep -E "Listening|pid" | awk -F '0800] ' '{print $2}' | awk -F '[' '{print $2}' | awk -F ']' '{print $1}'|xargs kill -9