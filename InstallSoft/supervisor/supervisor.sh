#!/bin/bash

sudo apt-get -y install supervisor
pip3 install supervisor
easy_install supervisor

# cd /etc/supervisor/conf.d/
# vim config.conf

#     [program:task]                                       #管理进程的命名
#     command=python test.py  -c test.conf　　　　　　　　　　#执行的命令
#     stderr_logfile=/var/log/supervisor/test.log　　　　　　#错误日志输出路径
#     stdout_logfile=/var/log/supervisor/test.log　　　　　　#日志输出路径
#     directory=/root/test　　　　　　　　　　　　　　　　　　　 #命令执行的工作空间
#     autostart=true　　　　　　　　　　　　　　　　　　　　　　　#自动启动
#     user=root　　　　　　　　　　　　　　　　　　　　　　　　　　#指定用户
#     autorestart=true　　　　　　　　　　　　　　　　　　　　　　#自动重启</pre>

# supervisorctl reload

#     supervisorctl status #查看supervisorctl状态
#     supervisorctl start nginx #启动子进程nginx
#     supervisorctl stop nginx  #关闭子进程nginx
#     supervisorctl restart nginx #重启子进程nginx
