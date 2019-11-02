#!/bin/bash
# cd /usr/local/share
# --upload python.tar.gz
# tree
#   .
#   └── python
#       ├── installPython.sh
#       └── Python-3.6.7.tgz
# cd python
# chmod +x ./installPython.sh
# ./installPython.sh


function pythonLib(){
    gcc --version
    if [ ! $? -eq 0 ];then
        yum -y install gcc
    fi
    zlib_devel=`rpm -qa|grep zlib-devel`
    if [ -z $zlib_devel ];then
        echo "Installing lib zlib..."
        yum -y install zlib*
    fi
    openssl_devel=`rpm -qa|grep openssl-devel`
    if [ -z $openssl_devel ];then
        echo "Installing lib openssl-devel..."
        yum -y install openssl
        yum -y install openssl-devel
        yum -y install openssl-static
    fi
    sqlite_devel=`rpm -qa|grep sqlite-devel`
    if [ -z $sqlite_devel ];then
        echo "Installing lib sqlite..."
        yum -y install sqlite
        yum -y install sqlite-devel
    fi
    yum -y install bzip2 bzip2-devel ncurses lzma libffi-devel
    yum -y install gdbm gdbm-devel tk tk-devel xz xz-devel
}

function pythonPage(){
    pageName=`find ./ -name "Python-*.tgz"|awk -F "/" '{print $2}'`
    if [ -z $pageName ];then
        return 1
    else
        tar -zxvf ./$pageName
    fi
}

function pythonMake(){
    fileName=`echo $pageName|awk -F ".tgz" '{print $1}'`
    installPath=`pwd`
    cd $fileName
    ./configure --prefix=$installPath --enable-optimizations --with-ssl --enable-shared CFLAGS=-fPIC
    make
    make install
    echo "$installPath/lib/" > /etc/ld.so.conf.d/$fileName.conf
    ldconfig
    cd $installPath
}

function install(){
    yum --version
    if [ ! $? -eq 0 ];then
        echo "Command yum is not found!"
        exit 1
    fi
    pythonLib
    if [ ! $? -eq 0 ];then
        echo "yum installation error!"
        exit 1
    fi
    pythonPage
    if [ $? -eq 1 ];then
        echo "No python installation package!"
        exit 1
    fi
    pythonMake
    if [ ! $? -eq 0 ];then
        echo "python installation failed!"
        exit 1
    else
        echo "python installation successful!"
    fi
}

function Main(){
    install
    cd /usr/local/bin
    lnName="./python3"
    if [ ! -e $lnName ];then
        ln -s $installPath/bin/python3 python3
        ln -s $installPath/bin/pip3 pip3
        if [ $? -eq 0 ];then
            echo "Soft link creation successful!"
        else
            echo "Soft link creation failed!"
        fi
    else
        echo "Soft link python3 already exists!"
    fi
}

Main

