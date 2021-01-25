#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   sy.py
@time:   2021-01-12 17:47:29
@description:
"""

import matplotlib.pyplot as plt
from datetime import datetime


PROFIT = {
    # '2020': 11833,
    # '2020_date': '2021/01/28'
}


def get_img(_t1, _t2):
    _t1 = tuple(_t1)
    _t2 = tuple(_t2)

    plt.figure(figsize=(12, 8))
    plt.title("Annual investment of 10,000 RMB, annualized rate of return is 18.33018023%.")

    plt.bar(x=_tup1, height=_tup2, width=0.5, align="center", label='profit')

    for _a, _b in zip(_tup1, _tup2):
        plt.text(_a, _b, round(_b), ha='center', va='bottom', fontsize=5)

    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':

    a = 0
    b = 1.1833018023
    c = 0
    d = 10000
    e = 0
    f = 0

    print("""|投资年份|投资金额|结算日期|本期结余|收益金额|收益总额|年化收益|累计收益|目标差值|""")
    print("""|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|""")

    _tup1 = []
    _tup2 = []

    for i in range(30):
        f = i + 1
        c = d * f
        a = (a + d) * b
        e = (a - c) / c * 100

        h = 2020 + i
        _tup1.append(h)
        _tup2.append(a)

        _dict = dict()

        i0 = PROFIT.get('{}'.format(h), None)
        i1 = PROFIT.get('{}'.format(h - 1), d)

        if i0:
            _dict['t'] = PROFIT.get('{}_date'.format(h))
            _dict['a'] = i0
            _dict['b'] = i0 - i1
            _dict['c'] = i0 - c
            _dict['d'] = round((i0 - i1) / i1 * 100, 2)
            _dict['e'] = round((i0 - c) / c * 100, 2)
            _dict['f'] = round((i0 - a) / a * 100, 6)

        if datetime.now().year >= h:
            print("""|{}|10000|{}|{}|{}|{}|{}|{}|{}|""".format(
                h,
                _dict.get('t', '-'),
                _dict.get('a', '-'),
                _dict.get('b', '-'),
                _dict.get('c', '-'),
                _dict.get('d', '-'),
                _dict.get('e', '-'),
                _dict.get('f', '-'),
            ))

    # get_img(_tup1, _tup2)
