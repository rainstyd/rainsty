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
        sudo apt-get -y install gcc
    fi
    sudo apt-get -y install zlib*
    sudo apt-get -y install openssl
    sudo apt-get -y install libssl-dev
    sudo apt-get -y install libffi-dev
    sudo apt-get -y install libsqlite3-dev
    sudo apt-get -y install build-essential checkinstall libc6-dev libbz2-dev
    sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev tk-dev libgdbm-dev
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
    sudo touch /etc/ld.so.conf.d/$fileName.conf
    sudo chmod 777 /etc/ld.so.conf.d/$fileName.conf
    echo "$installPath/lib/" > /etc/ld.so.conf.d/$fileName.conf
    sudo ldconfig
    cd $installPath
}

function install(){
    pythonLib
    if [ ! $? -eq 0 ];then
        echo "Error: Installation libs error!"
        echo "Please check if there is a download source available!"
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
        sudo ln -s $installPath/bin/python3 python3
        sudo ln -s $installPath/bin/pip3 pip3
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

