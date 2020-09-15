# Oracle安装  

* 目录结构  

``` text
root@rainsty:oracle# ll
total 2080904
-rw-r--r-- 1 root root        337 Sep 15 20:36 docker-compose.yml
drwxr-xr-x 2 root root       4096 Sep 15 20:37 volumes/
root@rainsty:oracle# ll volumes/
total 4
-rwxr-xr-x 1 root root 433 Sep 15 19:58 listener.ora
root@rainsty:oracle#
```

* 文件内容  

    [docker-compose.yml](../dockerFile/oracle/docker-compose.yml)
    [listener.ora](../dockerFile/oracle/volumes/listener.ora)
    
* 执行安装  

``` text
docker-compose up -d
vim volumes/listener.ora
docker cp volumes/listener.ora oracle:/u01/app/oracle/product/11.2.0/xe/network/admin
```

# Oracle命令  

* 进入容器  

``` text
docker exec -it oracle bash
```

* 进入Mysql终端  

``` text
sqlplus system/oracle
```

* 创建用户  

``` text
create user oracle identified by oracle;
```

* 查看是否有用户  

``` text
select * from all_users;
```

* 赋予远程登陆权限  

``` text
grant connect,resource,create session to oracle;
```

* 更改监听端口  

``` text
docker cp volumes/listener.ora oracle:/u01/app/oracle/product/11.2.0/xe/network/admin
docker-com restart
```
