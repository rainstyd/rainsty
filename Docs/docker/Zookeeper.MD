# Zookeeper安装

* 目录结构  

``` text
[root@kafka-0003 07_zook]# ll
总用量 8
-rw-r--r-- 1 root root 1312 7月  21 13:52 docker-compose.yml
```

* 文件内容  

    [docker-compose.yml](../dockerFile/zookeeper/docker-compose.yml)
  
* 执行安装  

``` text
docker-compose up -d
```

# Zookeeper命令

``` text
进入容器
docker exec -it zook01 bash

今日zk客户端
bin/zkCli.sh

执行查看目录命令
ls /
```
