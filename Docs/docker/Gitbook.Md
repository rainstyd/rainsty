# Gitbook镜像制作  

* 目录结构  

``` text
root@rainsty:~/rainsty/Docker/gitbook# ll image/
total 12
-rw-r--r-- 1 root root 376 Aug 13 13:22 Dockerfile
-rw-r--r-- 1 root root 140 Aug 13 13:22 run.sh
-rw-r--r-- 1 root root  41 Aug 13 13:22 start.sh
```

* 文件内容  

    [Dockerfile](../file/gitbook/image/Dockerfile)  
    [run.sh](../file/gitbook/image/run.sh)  
    [start.sh](../file/gitbook/image/start.sh)  

* 执行镜像制作  

``` text
bash start.sh
```

# Gitbook容器使用  

* 目录结构  

``` text
root@rainsty:~/rainsty/Docs/file/gitbook# ll
total 16
-rw-r--r-- 1 root root  312 Aug 13 14:40 docker-compose.yml
-rw-r--r-- 1 root root  144 Aug 13 14:40 run.sh
-rw-r--r-- 1 root root  233 Aug 13 14:40 start.sh
```

* 文件内容  

    [docker-compose.yml](../file/gitbook/docker-compose.yml)  
    [run.sh](../file/gitbook/run.sh)  
    [start.sh](../file/gitbook/start.sh)  

* 启动容器  

``` text
bash start.sh
```

* 登陆页面验证  

``` text
http://127.0.0.1:8080
```
