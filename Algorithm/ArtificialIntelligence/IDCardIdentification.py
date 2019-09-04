#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   IDCardIdentification.py
@time:   2019-07-10 09:12
@description: baidu aip, pip install baidu-aip
"""

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16751862'
API_KEY = 'Ir1gDqNYkLEPNybOhhegiFIq'
SECRET_KEY = 'K6xqdtbCAshnxiFaLN8NWGnLCC9AwoOW'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


path = '../../Test/file/picture/'
image = get_file_content(path + '1567605252774.jpg')

# idCardSide = "front"
# """ 调用身份证识别 """
# res = client.idcard(image, idCardSide)
# print(res)

""" 如果有可选参数 """
options = dict()
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
res = client.basicAccurate(image, options)
# print(res)
for r in res['words_result']:
    print(r['words'])
