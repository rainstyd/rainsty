#!/bin/bash

npm config get
npm config set registry http://registry.npm.taobao.org
gitbook init
gitbook install
gitbook build
gitbook serve
