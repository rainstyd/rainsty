# -*- encoding: utf-8 -*-

"""
@author:  rainsty
@file:    to_requests.py
@time:    2025-07-26 13:52:28
@version: v1.0.23
@description:

    1: 兼容多地址自动切换requests连接类
        version: v1.0.24
        update:  2025-08-25 13:24:28
        desc:    实例化时增加timeout入参

"""

import requests
import datetime


class ToRequests(object):

    def __init__(self, url_list, timeout=10):
        if isinstance(url_list, str):
            self.url_list = url_list.split(',')
        self.url_last = None
        self.timeout = timeout

    def to_send(self, method='GET', payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}

        response = None
        error_info = None

        if self.url_last:
            url_list = [self.url_last] + self.url_list
        else:
            url_list = self.url_list
        # print(url_list)

        for url in url_list:
            try:
                response = requests.request(method, url, headers=headers, data=payload, timeout=self.timeout)
                # print(response.text)
                if response.status_code == 200:
                    self.url_last = url
                    error_info = None
                    # print([datetime.datetime.now().__str__(), 'INFO', 'to_get', url])
                    break
                else:
                    # print([datetime.datetime.now().__str__(), 'ERROR', 'to_get', url])
                    continue
            except BaseException as e:
                error_info = [datetime.datetime.now().__str__(), 'ERROR', 'to_send', url, e.__traceback__.tb_lineno, e]
                # print(error_info)
        return response, error_info

    def to_get(self, method='GET', payload=None, headers=None):
        payload = payload if payload else {}
        headers = headers if headers else {}

        response = None
        error_info = None

        if self.url_last:
            url_list = [self.url_last] + self.url_list
        else:
            url_list = self.url_list
        # print(url_list)

        for url in url_list:
            try:
                url_end = url + '?' + '&'.join(['{}={}'.format(p, payload[p])for p in payload.keys()])
                response = requests.request(method, url_end, headers=headers, data=payload, timeout=self.timeout)
                # print(response.text)
                if response.status_code == 200:
                    self.url_last = url
                    error_info = None
                    # print([datetime.datetime.now().__str__(), 'INFO', 'to_get', url])
                    break
                else:
                    # print([datetime.datetime.now().__str__(), 'ERROR', 'to_get', url])
                    continue
            except BaseException as e:
                error_info = [datetime.datetime.now().__str__(), 'ERROR', 'to_send', url, e.__traceback__.tb_lineno, e]
                # print(error_info)
        return response, error_info


if __name__ == '__main__':
    to_requests = ToRequests('http://121.37.178.58:9101,http://121.37.178.58:8707', timeout=10)
    result, error = to_requests.to_send()
    # print(result, error)
    if not error:
        print(result.text)
    else:
        print(error)
