# Docker安装-Ubuntu系统  

``` text
sudo apt-get remove docker docker-engine docker.io -y
sudo apt-get update -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-get update -y
sudo apt-get install docker.io -y

```

# Docker安装-CentOS系统  

``` text
# docker官方一键安装
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```
