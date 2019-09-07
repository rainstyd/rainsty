#!/usr/bin/python
# -*- coding: utf-8 -*-# filename: basic.py
import urllib
import time
import json


class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        appId = "wx0ccdb059824ae839"
        appSecret = "3998a0bc947d0217b26ea41efe7c9da5"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
               "client_credential&appid=%s&secret=%s&scope=snsapi_userinfo" % (appId, appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        print urlResp
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
        f = open('./logs/basic.log', 'a')
        f.write('------------------------basic.py\n')
        f.write(urlResp['access_token'] + '\n')
        f.write(str(urlResp['expires_in']) + '\n')
        f.write('------------------------basic.py\n')
        f.close()

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        while(True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()


print Basic().get_access_token()
