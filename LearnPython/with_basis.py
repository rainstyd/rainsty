#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   with_basis.py
@time:   2019-11-13 22:03:40
@description:
"""

from contextlib import contextmanager


class Test(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, type, value, trace):
        print('__exit__')


with Test('Test') as t:
    print(t.name)


class Test01(object):

    def __init__(self, name, mode):
        self.__name = name
        self.__mode = mode

    def __enter__(self):
        self.__f = open(self.__name, self.__mode)
        return self.__f

    def __exit__(self, type, value, trace):
        self.__f.close()


with Test01('./a.out', 'a') as a:
    a.write('hello world!\n')


@contextmanager
def test02(name, mode):
    try:
        f = None
        f = open(name, mode)
        yield f
    except Exception as e:
        raise(e)
    finally:
        if f:
            f.close()


with test02('b.out', 'r') as r:
    print(r.readlines())

