#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   Re.py
@time:   2020-09-17 20:30:29
@description: [https://www.runoob.com/python/python-reg-expressions.html]
"""

import re


r"""remark
    print(re.__all__)

    index:
        re.match
        re.search
        re.sub
        re.compile
        re.findall
        re.finditer
        re.split

    正则表达式匹配规则
        模式	描述
        ^	        匹配字符串的开头
        $	        匹配字符串的末尾。
        .	        匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
        [...]	    用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
        [^...]	    不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
        re*	        匹配0个或多个的表达式。
        re+	        匹配1个或多个的表达式。
        re?	        匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
        re{ n}	    精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
        re{ n,}	    匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
        re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
        a| b	    匹配a或b
        (re)	    对正则表达式分组并记住匹配的文本
        (?imx)	    正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
        (?-imx)	    正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
        (?: re)	    类似 (...), 但是不表示一个组
        (?imx: re)	在括号中使用i, m, 或 x 可选标志
        (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
        (?#...)	    注释.
        (?= re)	    前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
        (?! re)	    前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
        (?> re)	    匹配的独立模式，省去回溯。
        \w	        匹配字母数字及下划线
        \W	        匹配非字母数字及下划线
        \s	        匹配任意空白字符，等价于 [\t\n\r\f].
        \S	        匹配任意非空字符
        \d	        匹配任意数字，等价于 [0-9].
        \D	        匹配任意非数字
        \A	        匹配字符串开始
        \Z	        匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
        \z	        匹配字符串结束
        \G	        匹配最后匹配完成的位置。
        \b	        匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
        \B	        匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
        \n, \t, 等  匹配一个换行符。匹配一个制表符。等。
        \1...\9	    匹配第n个分组的内容。
        \10	        匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

    flags:    
        修饰符	描述
        re.I	使匹配对大小写不敏感
        re.L	做本地化识别（locale-aware）匹配
        re.M	多行匹配，影响 ^ 和 $
        re.S	使 . 匹配包括换行在内的所有字符
        re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
        re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

    re.RegexObject:
        re.compile() 返回 RegexObject 对象。

    re.MatchObject
        group() 返回被 RE 匹配的字符串。
        start() 返回匹配开始的位置
        end() 返回匹配结束的位置
        span() 返回一个元组包含匹配 (开始,结束) 的位置

    match与search的区别:
        re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
        re.search匹配整个字符串，直到找到一个匹配。

    r = re.sub(r'(?P<value>\d+)', double, s):
        ?P<value>\d+:
            ?P: 定义一个分组，为re.match对象
            <value>: 传入re.match对象的分组名，可以用re.match.group('value')获取匹配到的值
            \d+: 传入repl函数的值的匹配规则
"""

# re.match(pattern, string, flags)
print('re.match(pattern, string, flags)-----------------------------------------')
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

# re.search(pattern, string, flags)
print('re.search(pattern, string, flags)----------------------------------------')
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

# re.sub(pattern, repl, string, count, flags)
print('re.sub(pattern, repl, string, count, flags)------------------------------')
s = '2004-959-559 # # # 这是一个国外电话号码'
r = re.sub(r' #.*?', '', s, count=2)
print(r)
"""
    2004-959-559 # 这是一个国外电话号码
    repl 可以是一个函数
"""


def double(matched):
    # print(matched)
    value = int(matched.group('value'))
    print(value)
    return str(value * 2)


def upper(matched):
    # print(matched)
    value = matched.group('value')
    print(value)
    return value.upper()


s = 'A2004c959D559e # # # 这是一个国外电话号码'
r = re.sub(r'(?P<value>\d+)', double, s)
print(r)
r = re.sub(r'(?P<value>[a-zA-Z]+)', upper, s)
print(r)

# re.compile(pattern, flags)
print('re.compile(pattern, flags)-----------------------------------------------')
pattern = re.compile(r'([a-z]+)[0-9]+([a-z]+)', re.I)
s = 'one12twothree34fourR'
m = pattern.match(s, 1, 30)
print(m)
print(m.span())
print(m.groups())
print(m.group(1))
print(m.group(2))
print(m.start(1))
print(m.end(1))
print(m.start(2))
print(m.end(2))

# re.findall(pattern, string, flags)
print('re.findall(pattern, string, flags)---------------------------------------')
s = 'one12twothree34fourR\noneD133PO2twFothreTe3UI4fourR'
r = re.findall(r'[a-z]+', s, re.I)
print(r)

# re.finditer(pattern, string, flags)
print('re.finditer(pattern, string, flags)--------------------------------------')
r = re.finditer(r'[a-z]+', s, re.I)
for it in r:
    """返回一个迭代器"""
    print(it.group())

# re.split(pattern, string, maxsplit, flags)
print('re.split(pattern, string, maxsplit, flags)-------------------------------')
"""maxsplit最大分割次数，默认全分割，分割次数+1 = 分割完成数组长度"""
s = 'oNe12twothree34fourRneD133PO2twFothr555eTe3UI4fourR'
r = re.split(r'[a-z]+', s, 5, re.I)
print(r)
print(len(r))
