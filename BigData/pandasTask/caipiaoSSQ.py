#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename: caipiaoSSQ.py
# cteatedtime: 2019-09-03


import pandas as pd
import json
import os


file_path = '../../ScrapyApp/caipiaoSSQ/my_ssq.json'
save_path = './my_ssq.txt'
if not os.path.exists(save_path):
    with open(file_path, 'r') as r, open(save_path, 'w') as w:
        w.write('one two thr fou fiv six sev')
        for line in r.readlines():
            line = str(json.loads(line)['开奖号码']).replace('+', ' ')
            print(line)
            w.write('\n' + line)

df = pd.read_csv(save_path)
print(df)
