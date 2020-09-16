# Python容器环境启动  

* 目录结构  

``` text
root@ubuntu:~/python# ll
total 8
-rw-r--r-- 1 root root  421 Sep 16 11:40 docker-compose.yml
drwxr-xr-x 3 root root 4096 Sep 16 12:29 volumes/
root@ubuntu:~/python# ll volumes/
total 12
drwxr-xr-x 2 root root 4096 Sep 16 11:40 file/
-rw-r--r-- 1 root root   31 Sep 16 11:40 requirements.txt
-rw-r--r-- 1 root root  486 Sep 16 12:29 run.sh
root@ubuntu:~/python#
```

* 文件内容  

    [docker-compose.yml](../dockerFile/python/docker-compose.yml)  
    [requirements.txt](../dockerFile/python/volumes/requirements.txt)  
    [run.sh](../dockerFile/python/volumes/run.sh)  

* 启动容器  

``` text
docker-compose up -d
```
