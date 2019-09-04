#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   re_basis.py
@time:   2019-09-04 10:21
@description: re
"""

import re

"""remark
    print(re.__all__)

    # [https://www.runoob.com/python/python-reg-expressions.html]
    
    flags:    
        修饰符	描述
        re.I	使匹配对大小写不敏感
        re.L	做本地化识别（locale-aware）匹配
        re.M	多行匹配，影响 ^ 和 $
        re.S	使 . 匹配包括换行在内的所有字符
        re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
        re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    
    match与search的区别:
        re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
        re.search匹配整个字符串，直到找到一个匹配。
"""


# re.match(pattern, string, flags) -------------------------------------------------------------------------------
string = 'Cats are smarter than dogs'
r = re.match(r'(c.*) are (.*?) than (.*s)', string, re.M | re.I)
try:
    """r cannot be None, otherwise an error will be reported."""
    print(r)
    print(r.span())
    print(r.group().__class__)
    print(r.group(1))
    print(r.group(2))
    print(r.group(3))
    # print(r.group(4))
except BaseException as e:
    print(e)


# re.search(pattern, string, flags) ------------------------------------------------------------------------------
string = 'Cats are smarter than dogs'
r = re.search(r'(Ar.*) (.*?) than (.*s)', string, re.M | re.I)
try:
    """r cannot be None, otherwise an error will be reported."""
    print(r)
    print(r.span())
    print(r.group().__class__)
    print(r.group(1))
    print(r.group(2))
    print(r.group(3))
    # print(r.group(4))
except BaseException as e:
    print(e)

