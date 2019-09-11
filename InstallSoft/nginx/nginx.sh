#!/bin/bash

apt-get install build-essential
apt-get install libtool

apt-get install nginx

#   nginx 启动
#   /usr/local/webserver/nginx/sbin/nginx -s reload            # 重新载入配置文件
#   /usr/local/webserver/nginx/sbin/nginx -s reopen            # 重启 Nginx
#   /usr/local/webserver/nginx/sbin/nginx -s stop              # 停止 Nginx
