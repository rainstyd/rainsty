# Redis安装  

* 目录结构  

``` text
(base) root@ubuntu:redis# ll
total 8
-rw-r--r-- 1 root root  393 Sep 17 18:22 docker-compose.yml
drwxr-xr-x 3 root root 4096 Sep 17 18:23 volumes/
(base) root@ubuntu:redis# ll volumes/
total 8
-rw-r--r-- 1 root root  354 Sep 17 18:22 run.sh
(base) root@ubuntu:redis#
```

* 文件内容  

    [docker-compose.yml](../dockerFile/redis/docker-compose.yml)
    [run.sh](../dockerFile/redis/volumes/run.sh)
    
* 执行安装  

``` text
echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf
# echo "net.core.somaxconn = 1024" >> /etc/sysctl.conf
cat /etc/sysctl.conf
sysctl -p
docker-compose up -d
```
