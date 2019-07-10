#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   IDCardIdentification.py
@time:   2019-07-10 09:12
@description:
"""

""" baidu aip
pip install baidu-aip
"""
# from PIL import Image
# import pytesseract
#
#
# class Languages:
#     CHS = 'chi_sim'
#     ENG = 'eng'
#
#
# def img_to_str(image_path, lang=Languages.ENG):
#     return pytesseract.image_to_string(Image.open(image_path), lang)
#
#
# print(img_to_str('../../file/picture/id_card.jpg', lang=Languages.CHS))

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16751862'
API_KEY = 'Ir1gDqNYkLEPNybOhhegiFIq'
SECRET_KEY = 'K6xqdtbCAshnxiFaLN8NWGnLCC9AwoOW'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# image = get_file_content('../../file/picture/WechatIMG3.jpeg')
# idCardSide = "front"
#
# """ 调用身份证识别 """
# res = client.idcard(image, idCardSide)
# print(res)

image = get_file_content('../../file/picture/WechatIMG3.jpeg')

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
res = client.basicAccurate(image, options)
print(res)
