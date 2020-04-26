#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename: caipiaoSSQ.py
# cteatedtime: 2019-09-03


import pandas as pd
import json
import os


file_path = '../../Spiders/ScrapyApp/caipiaoSSQ/my_ssq.json'
save_path = './my_ssq.txt'


def ssq_data():

    if not os.path.exists(save_path):
        with open(file_path, 'r') as r, open(save_path, 'w') as w:
            w.write('one two thr fou fiv six sev')
            for line in r.readlines():
                line = str(json.loads(line)['开奖号码']).replace('+', ' ')
                print(line)
                w.write('\n' + line)
        return 'Make file successful.'
    else:
        return 'This file is exists.'


def main():
    print(ssq_data())
    df = pd.read_csv(save_path, sep=' ')
    print(df)
    print(df.shape)
    print(df.info())
    print(df.dtypes)
    print(df['six'].dtype)
    print(df.isnull())
    print(df.columns)
    print(df.head(10))
    print(df.tail(10))
    df['row_sum'] = df.apply(lambda x: x.sum(), axis=1)
    df.loc['col_sum'] = df.apply(lambda x: x.sum())
    print(df)


if __name__ == '__main__':
    main()
