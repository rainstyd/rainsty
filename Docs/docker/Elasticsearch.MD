# ElasticSearch安装  

* 目录结构  

``` text
(base) root@ubuntu:elasticsearch# ll
total 8
-rw-r--r-- 1 root root 1575 Sep 17 17:02 docker-compose.yml
drwxrwxr-x 7 root root 4096 Sep 17 16:37 volumes/
(base) root@ubuntu:elasticsearch# ll volumes/
total 20
drwxrwxr-x 5 root root 4096 Sep 17 16:37 data/
drwxr-xr-x 2 root root 4096 Sep 17 16:36 es-01/
drwxr-xr-x 2 root root 4096 Sep 17 16:36 es-02/
drwxr-xr-x 2 root root 4096 Sep 17 16:36 es-03/
drwxrwxr-x 5 root root 4096 Sep 17 16:37 logs/

(base) root@ubuntu:elasticsearch# ll volumes/es-0*
volumes/es-01:
total 4
-rwxr-xr-x 1 root root 493 Sep 17 16:36 elasticsearch.yml*

volumes/es-02:
total 4
-rwxr-xr-x 1 root root 493 Sep 17 16:36 elasticsearch.yml*

volumes/es-03:
total 4
-rwxr-xr-x 1 root root 493 Sep 17 16:36 elasticsearch.yml*
```

* 文件内容  

    [docker-compose.yml](../dockerFile/elasticsearch/docker-compose.yml)
    [elasticsearch.yml-01](../dockerFile/elasticsearch/volumes/es-01/elasticsearch.yml)
    [elasticsearch.yml-02](../dockerFile/elasticsearch/volumes/es-02/elasticsearch.yml)
    [elasticsearch.yml-03](../dockerFile/elasticsearch/volumes/es-03/elasticsearch.yml)
    
* 执行安装  

``` text
echo "vm.max_map_count=655360" >> /etc/sysctl.conf
cat /etc/sysctl.conf
sysctl -p
docker-compose up -d
chmod 777 volumes/data/*
chmod 777 volumes/logs/*
docker-compose restart
```

# ElasticSearchHead安装  

* 目录结构  

``` text
(base) root@ubuntu:elasticsearchHead# ll
total 8
-rw-r--r-- 1 root root  453 Sep 17 17:02 docker-compose.yml
drwxr-xr-x 2 root root 4096 Sep 17 16:36 volumes/
(base) root@ubuntu:elasticsearchHead# ll volumes/
total 452
-rw-r--r-- 1 root root 460009 Sep 17 16:36 vendor.js
(base) root@ubuntu:elasticsearchHead#
```

* 文件内容  

    [docker-compose.yml](../dockerFile/elasticsearchHead/docker-compose.yml)
    [vendor.js](../dockerFile/elasticsearchHead/volumes/vendor.js)
    
* 执行安装  

``` text
docker-compose up -d
```
