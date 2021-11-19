# Docker镜像仓库搭建  

* 下载Harbor安装包  

``` text
wget http://harbor.orientsoft.cn/harbor-v1.5.0/harbor-offline-installer-v1.5.0.tgz
```

* 创建证书  

``` text
# 创建目录
mkdir -p /data/cert/
cd /data/cert/

# 创建证书, 替换以下127.0.0.1为当前服务器的外网地址或者域名domain
openssl genrsa -des3 -out 127.0.0.1.key 2048
openssl req -new -key 127.0.0.1.key -out 127.0.0.1.crt
cp 127.0.0.1.key 127.0.0.1.key.org

# 取消密码
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

# 修改如下配置:
hostname = 127.0.0.1:8088
ssl_cert = /data/cert/127.0.0.1.crt
ssl_cert_key = /data/cert/127.0.0.1.key
```

* 修改docker-compose.yml  

``` text
vim docker-compose.yml

# 修改container_name=nginx的映射端口, 更改页面访问端口
- 8088:80
```

* 执行安装  

``` text
./install.sh
```

* 验证安装结果  

``` text
http://127.0.0.1:8088

# 用户名和密码为：
username/password=admin/Harbor12345
# 登陆之后可修改密码，上面为超级管理员初始密码
```

# Docker镜像仓库使用  

* 新增Docker配置文件  

``` text
vim /etc/docker/daemon.json

# 新增如下内容
{
    "registry-mirrors": ["https://njrds9qc.mirror.aliyuncs.com"],
    "insecure-registries":["127.0.0.1:8088", "www.rainsty.com:8088"]
}
```

* 重启Docker  

``` text
systemctl daemon-reload && systemctl restart docker
```

* 登陆镜像仓库  

``` text
docker login 127.0.0.1:8088

# 输入账号密码：
admin/Harbor123456

```

* 拉取镜像仓库image文件  

``` text
docker pull 127.0.0.1:8088/library/image:tag
docker tag 127.0.0.1:8088/library/image:tag library/image:tag
```

* 制作镜像上传至镜像仓库  

``` text
docker build -t library/image:tag .

docker login 127.0.0.1:8080
docker tag library/image:tag 127.0.0.1:8088/library/image:tag
docker push 127.0.0.1:8088/library/image:tag
```

* 退出镜像仓库  

``` text
docker logout 127.0.0.1:8080
```
