# Kafka安装

* 目录结构  

``` text
[root@kafka-0003 kafka]# ll
总用量 8
-rw-r--r-- 1 root root 1312 7月  21 13:52 docker-compose.yml
```

* 文件内容  

    [docker-compose.yml](../dockerFile/kafka/docker-compose.yml)

* 修改kafka外网访问IP  

``` text
vim docker-compose.yml

# 修改每个节点的参数IP
 30     ¦ KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://192.168.0.179:9192
```
  
* 执行安装  

``` text
docker-compose up -d
```

# Kafka命令

``` text
# 进入容器
docker exec -it kafka01 bash

```
