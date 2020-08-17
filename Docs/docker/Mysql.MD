# Mysql安装  

* 目录结构  

``` text
root@rainsty:mysql# ll
total 8
-rw-r--r-- 1 root root  448 Aug 17 17:09 docker-compose.yml
drwxr-xr-x 4 root root 4096 Aug 17 17:41 volumes/
root@rainsty:mysql# ll volumes/
total 8
drwxr-xr-x 6  999 root 4096 Aug 17 17:41 data/
drwxr-xr-x 2 root root 4096 Aug 17 17:06 mysql.conf.d/
root@rainsty:mysql# ll volumes/mysql.conf.d/
total 4
-rw-r--r-- 1 root root 1938 Aug 17 17:06 my.cnf
```

* 文件内容  

    [docker-compose.yml](../dockerFile/mysql/docker-compose.yml)
    [my.cnf](../dockerFile/mysql/volumes/mysql.conf.d/my.cnf)
    
* 执行安装  

``` text
docker-compose up -d
```

# Mysql命令  

* 进入容器  

``` text
docker exec -it mysql bash
```

* 进入Mysql终端  

``` text
mysql -uroot -p123456
```

* 创建用户  

``` text
CREATE USER 'rainsty'@'%' IDENTIFIED BY '123456';
```

* 赋予Navicat登陆权限  

``` text
ALTER USER rainsty IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY '123456';
```

* 赋予远程登陆权限  

``` text
GRANT ALL PRIVILEGES ON *.* TO rainsty@'%';
```

* 刷新权限  

``` text
FLUSH PRIVILEGES;
```
