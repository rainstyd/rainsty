#!/bin/bash
#filename: start.sh
#cteatedtime: 2019-01-08

#mkdir scrapyApp
# cd scrapyApp
# scrapy startproject caipiaoSSQ
# cd caipiaoSSQ
# scrapy genspider ssq 17500.cn


function Main(){
    echo '' > nohup.out
    scrapy crawl ssq > nohup.out 2>&1

    name="./my_ssq.txt"

    if [ -e $name ];then
        cat my_ssq.txt > my_ssq.json
        rm -rf my_ssq.txt
        rm -rf ./caipiaoSSQ/__pycache__
        rm -rf ./caipiaoSSQ/spiders/__pycache__
    fi
    }

Main
