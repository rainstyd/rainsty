#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   sy.py
@time:   2021-01-12 17:47:29
@description:
"""

a = 0
b = 1.1833018023
c = 0
d = 10000
e = 0
f = 0
print('每年收益率：{}%'.format(str('%.8f' % ((b-1)*100))))
for i in range(30):
    f = i + 1
    c = d * f
    a = (a + d) * b
    e = (a - c) / c * 100
    print('第{}年，收益：{}，总收益率：{}'.format(f, str('%.2f' % a), str('%.2f' % e)))
