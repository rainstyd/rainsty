#!/bin/bash
#filename: start.sh
#cteatedtime: 2019-01-08

#mkdir scrapyApp
#cd scrapyApp
#/usr/rain/python/bin/scrapy startproject caipiaoSSQ
#cd caipiaoSSQ
#/usr/rain/python/bin/scrapy genspider ssq 17500.cn


function Main(){
    /usr/rain/python/bin/scrapy crawl ssq > nohup.out 2>&1

    name="./my_ssq.txt"

    if [ -e $name ];then
        cat my_ssq.txt > my_ssq.json
        rm -rf my_ssq.txt
    fi
    }

Main
