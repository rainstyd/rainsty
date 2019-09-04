#!/bin/bash

cat ./file/headers.txt |awk -F ': ' '{print "'\''" $1 "'\'': '\''" $2 "'\'',"}'