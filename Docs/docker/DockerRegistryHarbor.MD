## Docker镜像仓库搭建-基于Harbor  

* 1: 下载Harbor安装包  

``` text
wget http://harbor.orientsoft.cn/harbor-v1.5.0/harbor-offline-installer-v1.5.0.tgz
```

* 2: 创建证书  

``` text
创建目录
mkdir -p /data/cert/
cd /data/cert/

创建证书, 替换以下127.0.0.1为当前服务器的外网地址或者域名domain
openssl genrsa -des3 -out 127.0.0.1.key 2048
openssl req -new -key 127.0.0.1.key -out 127.0.0.1.crt
cp 127.0.0.1.key 127.0.0.1.key.org

取消密码
openssl rsa -in 127.0.0.1.key.org -out 127.0.0.1.key
openssl x509 -req -days 3650 -in 127.0.0.1.crt -signkey 127.0.0.1.key -out 127.0.0.1.crt
```  

* 解压Harbor安装包  

``` text
tar -zxvf harbor-offline-installer-v1.5.0.tgz
```

* 修改Harbor/harbor.cfg  

``` text
cd harbor && vim harbor.cfg

修改如下配置:
hostname = 127.0.0.1:8088
ssl_cert = /data/cert/127.0.0.1.crt
ssl_cert_key = /data/cert/127.0.0.1.key

vim docker-compose.yml

修改container_name=nginx的映射端口, 更改页面访问端口
       - 8088:80
```

* 执行安装  

``` text
./install.sh
```

* 验证安装结果  

``` text
http://127.0.0.1:8088

用户名和密码为：
username/password=admin/Harbor12345
```
