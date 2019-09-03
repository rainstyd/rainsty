#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   xpath-basis.py
@time:   2019-09-03 17:42
@description:
"""
import requests
from lxml import html
etree = html.etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''

html = etree.HTML(text)

print(html)
