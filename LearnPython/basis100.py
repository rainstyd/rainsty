#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# https://blog.csdn.net/weixin_41666747/article/details/79942847
# python 100 面试题
import random
import numpy as np
import pandas as pd
import re
import os
import sys
sys.path.append('./pythonApi/basis100')
import time
import json
import matplotlib.pyplot as plt
from functools import reduce
from datetime import datetime
from collections import Counter
from .pythonApi.basis100.singleton import singleton
from .pythonApi.basis100.test import test
from random import randint


def helloWorld():
    print('helloWorld...')
    return 'hello world!'


def test001():
    print('test001...')
    return sum(range(0, 101))

a = 0
def test002():
    print('test002...')
    global a
    print(a)
    a = 3
    return None
print(a)


def test003():
    print('test003...')
    print('sys')
    print('os')
    print('re')
    print('math')
    print('datetime')
    return 'test003'


def test004():
    print('test004...')
    dict = {"a": 1, "b": 2}
    del dict['a']
    print(dict)
    dict1 = {"c": 3, "d": 4}
    dict.update(dict1)
    return dict


def test005():
    print('test005...')
    return "GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），" \
        "使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所" \
        "以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。"


def test006():
    print('test006...')
    list = [1, 2, 3, 3, 4, 5, 6]
    list = [li for li in set(list)]
    return list


def test007():
    print('test007...')
    return "*args, **kwargs 能接收所有类型得参数，args为list，kwargs为dict"


def test008():
    print('test008...')
    return "python2: type <list>, python3: class <range>"


def test009():
    print('test009...')
    return "函数可以当作参数传递得语言，可以使用装饰器，python是动态的面向对象的编程语言。"


def test010():
    print('test010...')
    return "int bool str list tuple dict"


def test011():
    print('test011...')
    class A(object):
        def __init__(self, name):
            self.name = name
            print('这是__init__方法')

        def __new__(cls, name):
            print('这是__new__方法')
            return object.__new__(cls)
    A('rain')
    print(id(A))
    return "__init__ 是创建class之后的内置方法，可直接接收参数。__new__是实例化之前可以对当前类做修改，在__init__之前调用。"


def test012():
    print('test012...')
    with open('./file/basis100/test012.txt', 'a') as f:
        f.write('teset012')
    f = open('./file/basis100/test012.txt', 'r')
    try:
        print(f.read())
    except:
        pass
    finally:
        f.close()


def test013():
    print('test013...')
    list = [li for li in range(1, 6)]
    def fn(self):
        return self**2
    list = map(fn, list)
    list = [li for li in list if li > 10]
    return list


def test014():
    print('test014...')
    r = random.randint(0, 100)
    print(r)
    r = np.random.randn(5)
    print(r)
    r = np.random.random(10)
    return r


def test015():
    print('test015...')
    return "使用 r'' 可以避免字符串里面的内容转义。"


def test016():
    print('test016...')
    s = r'<div class="rain">中国</div>'
    r = re.findall(r'<div class=".*">(.*?)</div>', s)
    return r


def test017():
    print('test017...')
    a = 1
    # 为假，报错程序退出 断言。。。
    assert(a>=1)
    print(a)
    return a


def test018():
    print('test018...')
    return "select distinct name from student;"


def test019():
    print('test019...')
    return "cd ll ls grep ps awk echo vi vim mv cp scp lsof ss netstat nmap yum tar zip bash rm tail cat head more less ssh"


def test020():
    print('test020...')
    print('python3 print 必须用括号')
    print('python2 range list python range class')
    print('python2 ascii python3 utf-8')
    print('python2中unicode表示字符串序列，str表示字节序列, python3中str表示字符串序列，byte表示字节序列')
    print('python2中为正常显示中文，引入coding声明，python3中不需要。')
    print('python2中是raw_input()函数，python3中是input()函数。')
    return "python2 and python3 的区别。"


def test021():
    print('test021...')
    print('python3 中不可变数据类型 int str tuple')
    print('python3 中可以变数据类型 list dict')
    return "不可变类型改变内容生成新对象。"


def test022():
    print('test022')
    s = 'ajldjlajfdljfddd'
    s = set(s)
    s = list(s)
    s.sort()
    r = "".join(s)
    return r


def test023():
    print('test023...')
    sum = lambda a, b: a * b
    return sum(5, 4)


def test024():
    print('test024...')
    dict = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
    print(dict.items())
    list = sorted(dict.items(), key=lambda i: i[0], reverse=False)
    dict = {}
    for li in list:
        dict[li[0]] = li[1]
    return dict


def test025():
    print('test025...')
    s = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
    r = Counter(s)
    return r


def test026():
    print('test026...')
    a = "not 404 found 张三 99 深圳"
    l = a.split(' ')
    print(l)
    r = re.findall('\d+|[a-zA-Z]+', a)
    print(r)
    for i in r:
        if i in l:
            l.remove(i)
    s = " ".join(l)
    return s


def test027():
    print('test017...')
    l = [i for i in range(1, 11)]
    def fn(self):
        return self % 2 == 1
    l = filter(fn, l)
    return list(l)


def test028():
    print('test028...')
    l = [i for i in range(1, 11)]
    # return list(l)
    # l = filter(lambda x: x % 2 == 1, l)
    l = [i for i in l if i % 2 == 1]
    return l


def test029():
    print('test029...')
    return "re.compile是将正则表达式编译成一个对象，加快速度，并重复使用"


def test030():
    a = (1)
    b = ('1')
    c = (1, )
    print(a.__class__)
    print(b.__class__)
    print(c.__class__)
    return "类型测试。"


def test031():
    l1 = [1, 5, 7, 9]
    l2 = [2, 2, 6, 8]
    l1.append(3)
    l = l1 + l2
    l = sorted(l)
    return l


def test032():
    print('test032...')
    os.remove('./file/basis100/test012.txt')
    # rm -rf ./file/basis100/test012.txt
    return "删除成功"


def test033():
    print('test033...')
    # return int(time.mktime(datetime.strptime(str(datetime.now())[:-7], "%Y-%m-%d %H:%M:%S").timetuple())*1000)
    return int(time.mktime(datetime.now().timetuple()) * 1000)


def test034():
    print('test034...')
    with open('./file/basis100/sql.txt', 'r') as f:
        for i in f.read().split('\n'):
            if i != '':
                print(i)
    return "sql优化大全。"


def test035():
    print('test035...')
    _list = [dict(date='2017-11-10T00:01', count=65), dict(date='2017-11-10T00:02', count=55),
         dict(date='2017-11-10T00:03', count=61), dict(date='2017-11-10T00:04', count=52),
         dict(date='2017-11-10T00:05', count=57), dict(date='2017-11-10T00:06', count=55),
         dict(date='2017-11-10T00:07', count=61), dict(date='2017-11-10T00:08', count=52),
         dict(date='2017-11-10T00:09', count=57), dict(date='2017-11-10T00:10', count=55),
         dict(date='2017-11-10T00:11', count=61), dict(date='2017-11-10T00:12', count=52),
         dict(date='2017-11-10T00:13', count=57), dict(date='2017-11-10T00:14', count=55),
         dict(date='2017-11-10T00:15', count=61), dict(date='2017-11-10T00:16', count=52),
         dict(date='2017-11-10T00:17', count=57), dict(date='2017-11-10T00:18', count=55),
         dict(date='2017-11-10T00:19', count=61), dict(date='2017-11-10T00:20', count=52),
         dict(date='2017-11-10T00:21', count=57), dict(date='2017-11-10T00:22', count=55),
         dict(date='2017-11-10T00:23', count=61), dict(date='2017-11-10T00:24', count=52),
         dict(date='2017-11-10T00:25', count=57), dict(date='2017-11-10T00:26', count=55),
         dict(date='2017-11-10T00:27', count=61), dict(date='2017-11-10T00:28', count=52),
         dict(date='2017-11-10T00:29', count=57), dict(date='2017-11-10T00:30', count=55)]
    df = pd.DataFrame(data=_list)
    data = df.ix[0:24]
    data = data.set_index('date')
    data.index = pd.to_datetime(data.index)
    ts = data['count']
    ts.plot()
    plt.show()
    return "折线图。"


def test036():
    print('test037...')
    a = '1'
    try:
        a = a + 2
    except BaseException as e:
        raise TypeError('Type Error: %s' % e)


def test037():
    print('test037...')
    return ".* 为贪婪匹配，.*? 为最小匹配。"


def test038():
    print('test038')
    with open('./file/basis100/django.txt', 'r') as f:
        for t in f.read().split('\n'):
            print(t)
    with open('./file/basis100/orm.txt', 'r') as f:
        for t in f.read().split('\n'):
            print(t)
    return "百度词条信息。"


def test039():
    print('test039...')
    l = [[1, 2],[3, 4],[5, 6]]
    return reduce(lambda x, y: x + y, l)


def test040():
    print('test040...')
    x = "abc"
    y = "def"
    z = ["d", "e", "f"]
    return x.join(y)
    # return x.join(z)


def test041():
    print('test041...')
    try:
        f = open('./file/test041.txt', 'r')
        print(f.read())
        f.close()
    except BaseException as e:
        print(e)
    finally:
        return "test041"


def test042():
    print('test042...')
    a = 1
    b = 2
    a, b = b, a
    return a, b


def test043():
    print('test043...')
    l1 = [chr(i) for i in range(65, 91)]
    #l = [chr(i) for i in range(97, 123)]
    l2 = [i for i in range(1, 27)]
    return dict(zip(l1, l2))


def test044():
    print('test045...')
    a = "张明 98分"
    a = re.sub('98', '100', a)
    return a


def test045():
    print('test045...')
    print('select * from user;')
    print('select name,count(*) from user group by name')
    print('select count(*) from user;')
    print('select distinct name from user;')
    print('select id, name from user order by id desc limit 10;')
    return "sql 基础。"


def test046():
    print('test046...')
    a = 'hello'
    b = '你好'
    a = a.encode(encoding='utf-8')
    b = b.encode(encoding='utf-8')
    return b.decode(encoding='utf-8')


def test047():
    print('test047')
    a = [1, 2, 3]
    b = [4, 5, 6]
    return a + b


def test048():
    print('test048...')
    print('关键代码使用外部功能包：Cython, Pylnlne, PyPy, Pyrex')
    print('在排序时使用键')
    print('针对循环的优化')
    print('使用较新的python版本')
    print('尝试多种编码方式')
    print('交叉编译你的应用')
    return "python运行效率优化"


def test049():
    print('test049')
    print('mysql是关系型数据库，持久化数据，存入磁盘')
    print('redis是非关系型数据库，数据放入缓存，有保存时间限制')
    return "mysql与redis的区别"


def test050():
    print('test050...')
    print('确定错误类型')
    print('确定错误位置')
    print('查找错误原因')
    print('修复错误问题')
    print('测试是否解决')
    print('是否影响其他')
    return "遇到bug解决流程"


def test051():
    print('test051...')
    url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20' \
        '&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
    r = re.findall('\d{4}-\d{2}-\d{2}', url)
    for i in r:
        print(i)
    return "正则匹配所有"


def test052():
    print('test052...')
    l = [2, 3, 5, 4, 9, 6]
    print('排序前：')
    print(l)
    def _sort(l):
        li = []
        for i in range(len(l)):
            if len(li) == 0:
                li.append(l[i])
            else:
                for i1 in range(len(li)):
                    print(i, i1, len(li), l[i], li)
                    if i1 < len(li) -1 and (li[i1] <= l[i] < li[i1 +1]):
                        print('插入')
                        li.insert(i1+1,l[i])
                        break
                    elif i1 == len(li) - 1:
                        print('新增')
                        li.append(l[i])
        print('排序后：')
        return li
    return _sort(l)


def test053():
    print('test053...')
    sing = singleton
    return sing


def test054():
    print('test054...')
    a = "%.03f" % 1.3335
    print(a)
    #return round(float(a), 2)
    return round(float(1.3336), 3)


def test055():
    print('test055...')
    s = 'abc'
    print(s)
    print('%s' % s)
    return s


def test056():
    print('test056...')
    print('200 404 500 302 406')
    return "http 状态码。"


def test057():
    print('test057...')
    with open('./file/basis100/webyh.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return 'web优化。'


def test058():
    print('test058...')
    dic = {"name": "zs", "age": 18}
    #del dic['name']
    dic.pop('name')
    return dic


def test059():
    print('test059...')
    with open('./file/basis100/sqlyq.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "mysql三种存储引擎。"


def test060():
    print('test060...')
    l1 = [chr(l) for l in range(97, 102)]
    l2 = [l for l in range(1, 6)]
    return list(zip(l1, l2))


def test061():
    print('test061...')
    return "同源策略（Same origin policy）是一种约定，它是浏览器最核心也最基本的安全功能，如果缺少了同源策略，则浏览器的正常功能" \
        "可能都会受到影响。可以说Web是构建在同源策略基础之上的，浏览器只是针对同源策略的一种实现。"

def test062():
    print('test062...')
    with open('./file/basis100/cookiessession.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "cookie he session de qubie."


def test063():
    print('test063...')
    with open('./file/basis100/jinxian.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "多线程与多进程。"


def test064():
    print('test064...')
    return any([0, '', False]), all([0, 1, 2, 3, 4, 5])


def test065():
    print('test065...')
    with open('./file/basis100/error.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "错误名称及解释。"


def test066():
    print('test066...')
    return "copy 浅复制，给旧对象打上标签,用于新对象，deepcopy 深复制，克隆旧对象到新对象。"


def test067():
    print('test067...')
    with open('./file/basis100/mfff.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "魔法方法。"


def test068():
    print('test068...')
    return sys.argv


def test069():
    print('test069')
    g = (i for i in range(3))
    print(g)
    print(g.__next__())
    print(next(g))
    return g.__next__()


def test070():
    print('test070...')
    a = "  hehheh  "
    return a.rstrip(), a


def test071():
    print('test071...')
    l = [0, -1, 3, -10, 5, 9]
    l.sort()
    print(l)
    l = [0, -1, 3, -10, 5, 9]
    return sorted(l)


def test072():
    print('test072...')
    foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    print('暂时不知道怎么实现。')
    return sorted(foo, key=lambda x: x)


def test073():
    print('test073...')
    foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    print('暂时只能做到这样。')
    return sorted(foo, key=lambda x: abs(x) if x < 0 else x)


def test074():
    print('test074...')
    l1 = [chr(l) for l in range(97, 102)]
    l2 = [l for l in range(97, 102)]
    l = []
    d = dict(zip(l1, l2))
    for k, v in d.items():
        t = {'%s' % k: v}
        l.append(t)
    print(l)
    return sorted(l, key=lambda x: tuple(x)[0], reverse=True)


def test075():
    print('test075...')
    l1 = [chr(l) for l in range(97, 102)]
    l2 = [l for l in range(97, 102)]
    l = []
    d = dict(zip(l1, l2))
    for k, v in d.items():
        t = (k, v)
        l.append(t)
    print(l)
    return sorted(l, key=lambda x: x[0], reverse=True)


def test076():
    print('test076...')
    l1 = [chr(l) for l in range(97, 102)]
    l2 = [l for l in range(97, 102)]
    l = []
    d = dict(zip(l1, l2))
    for k, v in d.items():
        t = [k, v]
        l.append(t)
    print(l)
    return sorted(l, key=lambda x: x[0], reverse=True)


def test077():
    print('test077...')
    d = {k: randint(60,100) for k in ('abzdcy')}
    return dict(sorted(list(zip(d.keys(), d.values())), key=lambda x: x[0]))


def test078():
    print('test078...')
    d = {k: randint(60,100) for k in ('abzdcy')}
    return sorted(d.items(), key=lambda x: x[0])


def test079():
    print('test079...')
    print([l for l in range(1, 6)])
    print([{"%s" % chr(k): v} for k, v in zip(range(97, 102), range(1, 6))])
    return {s for s in [1, 1, 2, 3, 4, 5, 6, 5, 6, 7]}


def test080():
    print('test080...')
    s = 'fasfsad,fsadfasdf,fsdafasdfsdfasf,fdssdafasdfsadfas,fs,fsdfd,fsdf,fsfsfs,fsdfsdf'
    l = [(k, len(k)) for k in s.split(',')]
    return ','.join(list(dict(sorted(l, key=lambda x: x[1])).keys()))


def test081():
    print('test081...')
    with open('./file/basis100/sqlzr.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "sql注入。"


def test082():
    print('test082...')
    s = "info:xiaoZhang 33 shandong"
    s = re.split(' |:', s)
    return s


def test083():
    print('test083...')
    s = '1423432@qq.com,142342423@163.com,435353453@ali.com,5346663634@163.com'
    s = re.findall('\d*@163.com', s)
    return s


def test084():
    def _fn(self, result):
        if self == 1:
            return result
        else:
            return _fn(self -1, self + result)
    print('尾递归函数。')
    return _fn(100, 1)


def test085():
    print('test085...')
    d = [(chr(k), k - 96) for k in range(97, 102)]
    d = {k: v for k, v in d}
    return json.dumps(d), json.loads(json.dumps(d)).__class__


def test086():
    print('test086...')
    with open('./file/basis100/mymi.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r.replace(' ', ''))
    return "m i 模式差距。"


def test087():
    print('test087...')
    s = 'fsdafihafksdjgsahfusdihfusfyldijflsafjklahvioandsiuinjscsudabfeabdsuvbdsajhfyejbacdsajybfdsjfbdsyfjbsdfdshaflhchuizxhccishudaf'
    l1 = []
    l2 = []
    def _map(self):
        if self in l1:
            l2[l1.index(self)] = l2[l1.index(self)] + 1
        elif self not in l1:
            l1.append(self)
            l2.append(1)
    for ss in s:
        _map(ss)
    print(l1, l2)
    d = {}
    def _map1(self):
        if self not in d.keys():
            d['%s' % self] = 1
        elif self in d.keys():
            d['%s' % self] = d['%s' % self] + 1
    for ss in s:
        _map1(ss)
    print(d)
    r = re.findall('s', s)
    return len(r)


def test088():
    print('test088...')
    s = 'fsdafasfjljfljsf'
    s = s.upper()
    print(s)
    return s.lower()


def test089():
    print('test089...')
    s = 'fsafn fjsalf sadl jsd fhsadfjksa fjla sjfl asfa fjdsal fjalsd jfal '
    print(s.replace(' ', ''))
    print(re.sub(' ', '', s))
    return "去空格"


def test090():
    print('test090...')
    s = '432432423423423,432432432,432432423,42342354,5453634634,543345435347,'
    r = re.findall('\d*[^4^7],', s)
    return r


def test091():
    print('test091...')
    with open('./file/basis100/pyjsjz.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "python 计数机制。"


def test092():
    print('test092...')
    #return int('1.4'), int(1.4)
    return int(1.4)


def test093():
    print('test093...')
    with open('./file/basis100/mmgf.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "命名规范。"


def test094():
    s = "https://blog.csdn.net/qq_38819293/article/details/81570751"
    r = re.findall('http.:\/\/[a-zA-Z]*\.[a-zA-Z]*\.[a-zA-Z]*\/[a-z]{2}_\d*\/[a-zA-Z]*\/[a-zA-Z]*\/\d*', s)
    return r


def test095():
    print('test095...')
    s = '我爱中国,fsalfjsfljljlfjl4r4l554r5'
    r = re.findall('[\u4E00-\u9FA5]', s)
    return r


def test096():
    print('test096...')
    with open('./file/basis100/lbs.txt', 'r') as f:
        for r in f.read().split('\n'):
            if r != '':
                print(r)
    return "乐观锁与悲观锁简介。"


def test097():
    print('test097...')
    print('r 只读模式')
    print('rb 二进制只读模式')
    print('r+ 读写模式')
    print('rb+ 二进制读写模式')
    return "文件读写"


def test098():
    print('test098...')
    print('> 写入覆盖')
    print('>> 写入追加')
    return "linux 基础"


def test099():
    print('test099...')
    s = "<html><h1>www.itcast.cn</h1></html>fsdfdsfsadfasf<>fsdfdsfsdfsd>?fdsf"
    s = re.findall(r'<html><h1>www.itcast.cn</h1></html>', s)
    return s


def test100():
    print('test100...')
    p = "I love you"
    print(id(p))
    def _param(p):
        return id(p)
    return _param(p)


if __name__ == '__main__':
    print(helloWorld())
    print(test001())
    print(test002())
    print(a)
    print(test003())
    print(test004())
    print(test005())
    print(test006())
    print(test007())
    print(test008())
    print(test009())
    print(test010())
    print(test011())
    print(test012())
    print(test013())
    print(test014())
    print(test015())
    print(test016())
    print(test017())
    print(test018())
    print(test019())
    print(test020())
    print(test021())
    print(test022())
    print(test023())
    print(test024())
    print(test025())
    print(test026())
    print(test027())
    print(test028())
    print(test029())
    print(test030())
    print(test031())
    print(test032())
    print(test033())
    print(test034())
    print(test035())
    try:
        print(test036())
    except:
        print('error......')
    print(test037())
    print(test038())
    print(test039())
    print(test040())
    print(test041())
    print(test042())
    print(test043())
    print(test044())
    print(test045())
    print(test046())
    print(test047())
    print(test048())
    print(test049())
    print(test050())
    print(test051())
    print(test052())
    print(test053())
    print(test053())
    print('test...')
    print(test())
    print(test054())
    print(test055())
    print(test056())
    print(test057())
    print(test058())
    print(test059())
    print(test060())
    print(test061())
    print(test062())
    print(test063())
    print(test064())
    print(test065())
    print(test066())
    print(test067())
    print(test068())
    print(test069())
    print(test070())
    print(test071())
    print(test072())
    print(test073())
    print(test074())
    print(test075())
    print(test076())
    print(test077())
    print(test078())
    print(test079())
    print(test080())
    print(test081())
    print(test082())
    print(test083())
    print(test084())
    print(test085())
    print(test086())
    print(test087())
    print(test088())
    print(test089())
    print(test090())
    print(test091())
    print(test092())
    print(test093())
    print(test094())
    print(test095())
    print(test096())
    print(test097())
    print(test098())
    print(test099())
    print(test100())
    print('python是地址传递')
