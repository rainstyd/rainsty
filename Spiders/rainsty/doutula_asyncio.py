#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   doutula_asyncio.py
@time:   2019-09-05 22:48:52
@description:
"""

import requests
from lxml import etree
from datetime import datetime
import asyncio
import asyncio


def get_html_xpath(url, xpath):
    resp = requests.get(url)
    code = resp.encoding
    # print(resp.text.encode(code).decode('utf-8'))
    html = etree.HTML(resp.text.encode(code).decode('utf-8'))
    results = html.xpath(xpath)
    result = list()
    for r in results:
        try:
            result.append(r.attrib)
        except BaseException as e:
            print(e)
            pass

    return result


def main():
    urls = [r['href'] for r in get_html_xpath('https://www.doutula.com/', '//div[@class="col-sm-9 center-wrap"]/a')]

    for url in urls:
        res = get_html_xpath(url, '//li[@class="list-group-item"]//a/img')
        try:
            for r in res:
                print(r['src'])
        except BaseException as e:
            print(e)
            pass


if __name__ == '__main__':
    print(datetime.now())
    main()
    print(datetime.now())
    print(datetime.now())
    print(datetime.now())
    print(datetime.now())
    print(datetime.now())
    print(datetime.now())

