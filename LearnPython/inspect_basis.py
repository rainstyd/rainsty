#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   inspect_basis.py
@time:   2019-09-18 19:51:24
@description:
"""

import inspect


def f(a=None, b=None):
    print(a)


a = inspect.getargspec(f)
print(a.args)
print(a.defaults)
