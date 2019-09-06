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
import aiohttp
import time

FILE_PATH = '../../Test/file/picture/'


def get_url_results(url, xpath):
    resp = requests.get(url)
    html = etree.HTML(resp.text.encode(resp.encoding).decode('utf-8'))
    return html.xpath(xpath)


def get_html_xpath(url, xpath):
    results = get_url_results(url, xpath)
    result = list()
    for r in results:
        try:
            result.append(r.attrib)
        except BaseException as e:
            print('git urls error: %s.' % e)

    return result


async def save_img(content, file_path):
    with open(file_path, 'wb') as w:
        w.write(content)


async def download_img(url):
    try:
        filename = url.split('/')[-1]
        file_path = FILE_PATH + filename

        content=""
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                response = await session.get(url, timeout=60)
                content = await response.read()
                await session.close()
        except BaseException as e:
            print('contant error:' + str(e))

        await save_img(content, file_path)

    except BaseException as e:
        print('download_img error: ' + str(e))


async def get_html_url_xpath(url, xpath):
    results = get_url_results(url, xpath)
    for r in results:
        await download_img(r.attrib['src'])


def main():
    urls = [r['href'] for r in get_html_xpath('https://www.doutula.com/', '//div[@class="col-sm-9 center-wrap"]/a')]

    try:
        tasks = [asyncio.ensure_future(get_html_url_xpath(url, '//li[@class="list-group-item"]//a/img')) for url in urls]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
    except BaseException as e:
        print('loop error: %s' % e)


if __name__ == '__main__':
    start = datetime.now()
    main()
    end = datetime.now()
    print('Sum the time is: {}S'.format(end - start))

