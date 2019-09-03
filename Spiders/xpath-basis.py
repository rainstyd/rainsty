#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   xpath-basis.py
@time:   2019-09-03 17:42
@description:
"""
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
for r in results:
    print(r.tag)
    print(r.text)
    print(r.attrib)
