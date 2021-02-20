#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   stock.py
@time:   2021-02-01 10:59:29
@description:   1: tdx更新日K数据
                2: tdx34数据导出功能
                3: tdx34高级导出功能
                4: tdx选择沪深A股和999999/399001
                5: tdx选择导出文件目录/格式开始导出数据
                6: 导出完成执行python -u stock.py
                7: 登陆东方财富终端创建新分组
                8: 功能/自选导入/高级选项/选择文件导入自选股
"""

import os
import datetime as dt
import pandas as pd


NAMES = ['date', 'open', 'high', 'low', 'close', 'volume', 'turnover', 'change', 'trend']
DATES = (dt.datetime.now() - dt.timedelta(days=365)).strftime('%Y%m%d')
FILES = './hqdata/'
INDEX = ['999999', '399001']


def get_files(_dir):
    _files = list(os.walk(_dir))[0][2]
    return _files


def get_data(_market, _stock):
    _df = pd.read_table('{}{}#{}.txt'.format(FILES, _market, _stock), encoding='GBK', skiprows=[0, 1], names=NAMES)
    _df = _df.drop(_df.shape[0] - 1)
    return _df


def get_change(_df):
    _change = []
    _trend = []

    for index in _df.index:
        _c = 0
        _t = 0
        if index > 0:
            last = _df.iloc[index - 1][4]
            end = _df.iloc[index][4]
            _c = round((end - last) / last * 100, 2)
            _t = 1 if end - last > 0 else 0
        _change.append(_c)
        _trend.append(_t)
    _df['change'] = _change
    _df['trend'] = _trend
    return _df


def filter_date(_df, _date):
    _df = _df[_df['date'] >= str(_date)]
    return _df


def get_sh():
    _df = get_data('SH', 999999)
    _df = get_change(_df)
    _df = filter_date(_df, DATES)
    return _df


def get_sz():
    _df = get_data('SZ', 399001)
    _df = get_change(_df)
    _df = filter_date(_df, DATES)
    return _df


def main():
    df_sh = get_sh()['trend']
    df_sz = get_sz()['trend']

    _result = []

    files = get_files(FILES)
    for i in range(len(files)):

        f = files[i].split('#')
        stock = f[1][:-4]
        market = f[0]

        if stock not in INDEX:
            _dict = dict()
            _r = []
            if market == 'SH':
                _df = get_data(market, stock)
                _df = get_change(_df)
                _df = filter_date(_df, DATES)
                try:
                    _change = (_df.iloc[-1]['close'] - _df.iloc[0]['close']) / _df.iloc[-1]['close'] * 100
                except (BaseException,):
                    _change = 0
                _change = round(_change, 2)
                _df = _df['trend']
                for a, b in zip(_df, df_sh):
                    if a == b:
                        _r.append(1)
                    else:
                        _r.append(0)

                _dict['stock'] = stock
                if _change > 0:
                    _dict['change'] = _change
                    if len(_r) == df_sh.count():
                        _dict['success'] = round(sum(_r) / len(_r) * 100, 2)
                        _result.append(_dict)
                else:
                    _dict['change'] = 0
                    _dict['success'] = 0

            if market == 'SZ':
                _df = get_data(market, stock)
                _df = get_change(_df)
                _df = filter_date(_df, DATES)
                try:
                    _change = (_df.iloc[-1]['close'] - _df.iloc[0]['close']) / _df.iloc[-1]['close'] * 100
                except (BaseException,):
                    _change = 0
                _change = round(_change, 2)
                _df = _df['trend']
                for a, b in zip(_df, df_sz):
                    if a == b:
                        _r.append(1)
                    else:
                        _r.append(0)

                _dict['stock'] = stock
                if _change > 0:
                    _dict['change'] = _change
                    if len(_r) == df_sz.count():
                        _dict['success'] = round(sum(_r) / len(_r) * 100, 2)
                        _result.append(_dict)
                else:
                    _dict['change'] = 0
                    _dict['success'] = 0

            print(_dict, i + 1)

    data = list(sorted(_result, key=lambda x: x['success'], reverse=True))[0:200]

    with open('stock_result.txt', 'w') as w:
        for d in data:
            w.write('{}\n'.format(d))

    with open('stock_result_end.txt', 'w') as w:
        for d in data:
            w.write('{}\n'.format(d.get('stock')))


if __name__ == '__main__':
    main()
