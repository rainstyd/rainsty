#!/bin/bash

# vim for python3-dev
#
# mkdir ~/vim
# cd ~/vim
#
# git clone https://github.com/vim/vim.git
#
# --> root@rainsty:~/vim# ll
# --> total 8
# --> -rw-r--r--  1 root root   77 Sep  8 20:49 installVim-ubuntu.sh
# --> drwxr-xr-x 11 root root 4096 Sep  8 20:52 vim/
# --> root@rainsty:~/vim#
# ./installVim-ubuntu.sh


function vimLib(){
    sudo apt-get -y install python3-dev
}


function vimPage(){
        if [ ! -d "./vim" ];then
            git clone https://github.com/vim/vim.git
        else
            echo "Start install vim..."
        fi
}


function vimMake(){
    python_config_dir="~/python/lib/python3.6/config-3.6m-x86_64-linux-gnu"
    vim_install_dir=`pwd`
    cd $vim_install_dir/vim
    ./configure --with-features=huge --enable-multibyte --enable-python3interp=yes --with-python3-config-dir=$python_config_dir --enable-gui=gtk2 --enable-cscope --prefix=$vim_install_dir
    make
    make install
    $vim_install_dir/bin/vim --version
}


function main(){
    vimLib
    vimPage
    vimMake
    if [ ! $? -eq 0  ];then
        echo "vim installation failed!"
    exit 1
        else
            echo "vim installation successful!"
            ln -s $vim_install_dir/bin/vim /usr/local/bin/vim
    fi
}

main

