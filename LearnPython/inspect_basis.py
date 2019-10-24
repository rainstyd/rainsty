#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   inspect_basis.py
@time:   2019-09-18 19:51:24
@description:
"""
"""
inspect模块主要提供了四种用处：

　　1.对是否是模块、框架、函数进行类型检查

　　2.获取源码

　　3.获取类或者函数的参数信息

　　4.解析堆栈
"""

import inspect


def f(a=None, b=None):
    print(a)


a = inspect.getargspec(f)
print(a.args)
print(a.defaults)
