#!/bin/bash

sudo passwd root
su root
apt-get install ssh -y
apt-get install vim -y
vim /etc/ssh/sshd_config
# :28 跳转到28行 PermitRootLogin 取消该行注释，将prohibit-password修改为yes
vim /etc/hostname

cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
apt-get remove iptables -y

sudo vi /etc/network/interfaces

iface ens33 inet static
address 192.168.1.163
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 114.114.114.114

reboot

vim install_docker.sh

sudo apt-get remove docker docker-engine docker.io -y
sudo apt-get update -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-get update -y
sudo apt-get install docker.io -y

bash install_docker.sh
apt-get install docker-compose -y

vi /etc/docker/daemon.json
{
    "registry-mirrors": ["https://hub-mirror.c.163.com"],
    "insecure-registries":["127.0.0.1:8088"]
}
{
    "insecure-registries":
    [
          "repo.tzt.cn:8088",
          "repo.tzt.cn:8085"
    ]
}
systemctl daemon-reload && systemctl restart docker
docker pull 127.0.0.1:8088/alarm/zookeeper:v1


swapoff -a
vim /etc/hsab
# 注释swap

vi /etc/sysctl.d/kubernetes.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
sysctl -p
modprobe br_netfilter
lsmod | grep br_netfilter

sudo apt update && sudo apt install -y apt-transport-https curl
curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -

echo "deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list

sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
