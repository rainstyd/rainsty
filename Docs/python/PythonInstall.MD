# Conda安装  

* 下载miniconda安装包  

``` text
# 清华大学软件下载站: https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/?C=M&O=D
mkdir /root/miniconda3_install && cd /root/miniconda3_install
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

* 目录结构  

``` text
root@ubuntu:~/miniconda3_install# ll
total 90872
-rw-r--r-- 1 root root 93052469 Jul 29 00:13 Miniconda3-latest-Linux-x86_64.sh
```

* 执行安装  

``` text
bash Miniconda3-latest-Linux-x86_64.sh
# 按enter--三下空格--输入yes--按enter--输入yes
source ~/.bashrc
```

* 配置镜像源  

``` text
vim /root/.condarc
# 插入一下内容
    ssl_verify: true
    channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
      - defaults
    show_channel_urls: true
    pip_interop_enabled: false
```

* 执行卸载  

``` text
(base) root@ubuntu:~# rm -rf /root/miniconda3
(base) root@ubuntu:~# rm -rf /root/.conda*
(base) root@ubuntu:~# vim /root/.bashrc
# 删除如下内容
    101 # >>> conda initialize >>>
    102 # !! Contents within this block are managed by 'conda init' !!
    103 __conda_setup="$('/root/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    104 if [ $? -eq 0 ]; then
    105     eval "$__conda_setup"
    106 else
    107     if [ -f "/root/miniconda3/etc/profile.d/conda.sh" ]; then
    108     ¦   . "/root/miniconda3/etc/profile.d/conda.sh"
    109     else
    110     ¦   export PATH="/root/miniconda3/bin:$PATH"
    111     fi
    112 fi
    113 unset __conda_setup
    114 # <<< conda initialize <<<

source /root/.bashrc
source /etc/profile
# 关闭当前终端，打开新终端:
echo $PATH
```

# Conda命令  

* 查看虚拟环境  

``` text
conda env list
# 或者
conda info -e
```

* 创建虚拟环境  

``` text
conda create -n rainsty python=3.6.5
```

* 进入虚拟环境  

``` text
conda activate rainsty
```

* 退出虚拟环境  

``` text
conda deactivate
```

# python的docker容器环境安装  

* [安装文档地址](../docker/Python.MD)
