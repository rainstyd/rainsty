# Consul: Docker容器跨服务器通信  

* 目录结构  

``` text
[root@kafka-001-0002 05_consul]# ll
总用量 4
-rw-r--r-- 1 root root 458 7月  15 09:44 docker-compose.yml
```

* 文件内容  

    [docker-compose.yml](../dockerFile/consul/docker-compose.yml)

* 更改docker配置  

``` text
cd /etc/systemd/system/multi-user.target.wants && vim docker.service

更改内容如下
ExecStart=/usr/local/bin/dockerd -H fd:// \
         --cluster-store=consul://192.168.0.218:8500 --cluster-advertise=eth0:2376
```

* 重启docker服务  

``` text
sudo systemctl daemon-reload && sudo systemctl restart docker
```

* 创建overlay容器跨服务器通信网桥  

``` text
docker network create -d overlay consul_overlay
```

* 启动consul容器  

``` text
docker network create rainsty
docker-compose up -d
```

* 进行测试  

``` text
在服务器一上执行
docker run -di --network consul_overlay --name my_centos1 centos:7

在服务器二上执行
docker run -di --network consul_overlay --name my_centos2 centos:7

拿到my_centos2的容器IP，如：172.17.0.3
docker network ls inspect consul_overlay

在服务器一上执行通信测试  
docker exec -it my_centos1 ping 172.17.0.3

ping成功说明部署成功
```
