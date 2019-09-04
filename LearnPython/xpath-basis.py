#!/usr/bin/python
# encoding: utf-8

import requests
from lxml import etree

"""
@author: rainsty
@file:   xpath-basis.py
@time:   2019-09-03 17:42
@description:
"""

"""Example
    from lxml import etree
    
    text = '''
    <div>
       <ul>
         <li name="wjk" class="two">wjk</li>
        <li name="wang" class="three">wang</li>
        <li name="karry" class="four">karry</li>
       </ul>
    </div>
    '''
    
    html = etree.HTML(text)
    results = html.xpath('//li')
    print(results)
    for r in results:
        print(r.tag)
        print(r.text)
        print(r.attrib)

"""


def get_html_xpath(xpath):
    url = 'http://www.jinxiaoke.com/'
    resp = requests.get(url)
    code = resp.encoding
    # print(resp.text.encode(code).decode('utf-8'))
    html = etree.HTML(resp.text.encode(code).decode('utf-8'))
    results = html.xpath(xpath)
    return [(r.text, r.attrib) for r in results if r.text is not None]


def main():
    print(get_html_xpath('/html/body/div[1]/section[5]/div[@class="container"]/div[1]/div[2]//p'))
    print(get_html_xpath('/html/body/div[1]/section[5]/div[@class="container"]/div[1]/div[2]/p'))
    print(get_html_xpath('/html/body/div[1]/section[5]/div[@class="container"]/div[1]/div[2]/p[last()-2]'))
    print(get_html_xpath('/html/body/div[1]/section[5]/div[@class="container"]/div[1]/div[2]/p[position()<2]'))


if __name__ == '__main__':
    main()
