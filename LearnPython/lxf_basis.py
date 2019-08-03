#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   lxf_basis.py
@time:   2019-08-01 15:48
@description:
"""

from collections.abc import Iterator
from functools import reduce
from datetime import datetime
import functools
from enum import Enum
import os
import threading
import time


# s = input()
# s = s.upper()
# print(s)
# print(s.__class__)

# This is a remark
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

for r in range(1, 10):
    if r > 5:
        print(r)
else:
    print('111')

try:
    a = 1
    a = str(a)
    a.upper()
except BaseException as e:
    print(e)
else:
    print('222')

a = 2
while a < 5:
    if a > 5:
        break
    else:
        a += 1
else:
    print('333')

a = 0.00000001
print(a)

a = 'sfjoanfdainfa'
a = set(a)
a = list(a)
a = sorted(a)
print(''.join(a))

a = 'a'
ord(a)
print(ord(a))

print(chr(444))
print(ord('我'), ord('爱'), ord('你'))

a = 'aaa'
print(a.encode('ascii').__class__)

a = '中'
print(a.encode('utf-8').decode('utf-8'))

a = 1
a = int(1)
print(a)

l = [1, 2, 3, 4]
l.append(5)
l.pop()
l.pop(3)
print(l)

d = dict(
    a=1,
    b=2,
    c=3
)
d.pop('a')
print(d)

s = set(l)
print(s)
s.add(4)
print(s)
s.pop()
print(s)
s.remove(4)
print(s)
s.pop()
print(s)
s.clear()
print(s)

s1 = set([1, 2, 3])
s2 = set([1, 2, 4])
print(s1 & s2)
print(s1 | s2)

l = [1, 3, 4, 6, 9, 0]
max = l[0]
min = l[0]
for r in l:
    if max < r:
        max = r
    if min > r:
        min = r
print(max)
print(min)

a = list(range(1, 4))
print(a.__class__)
g = (x for x in range(1, 4))
print(g.__class__)
a = iter(a)
print(a.__class__)
print(next(a))
print(next(a))

print(isinstance(a, Iterator))
print(isinstance(iter([]), Iterator))


def f(x, y, z):
    return x * y + z


l = map(f, range(1, 10), range(11, 20), range(21, 30))

print(list(l))


def f(x, y):
    return x * 10 + y


s = reduce(f, range(1, 10))
print(s)
s = reduce(lambda x, y: x + y, range(1, 10))
print(s)


def primes():
    yield 2
    i = 1
    while True:
        i += 2
        for j in range(2, int(i / 2 + 1)):
            if i % j == 0:
                break
        else:
            yield i


f = primes()
for a in range(1, 10):
    print(next(f))


def primes():
    yield 2

    def _odd_iter():
        i = 1
        while True:
            i += 2
            yield i

    def _not_divisible(j):
        return lambda x: x % j > 0

    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


f = primes()
for a in range(1, 10):
    print(next(f))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

l = sorted(L, key=lambda x: x[1], reverse=True)
print(l)


def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum


f = lazy_sum(1, 3, 5)
print(f)
print(f())


def f(x, y):

    def n(z):
        nonlocal x
        x = 3
        return x * y + z
    return n


f = f(2, 3)
print(f(5))


def log2(func):
    @functools.wraps(func)
    def w(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return w


def log3(text):
    def log(func):
        @functools.wraps(func)
        def w(*args, **kwargs):
            print('call %s(): the param is %s.' % (func.__name__, text))
            return func(*args, **kwargs)
        return w
    return log


@log2
@log3('decorator')
def now():
    return datetime.now()


print(now())
print('the function name is:', now.__name__)


int2 = functools.partial(int, base=2)
print('二进制转10进制，使用便函数partial实现:', int2('10001001'))


class Student(object):

    __slots__ = ('__name', '__age', 'a', 'b', 'c', 'd')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.a = 0
        self.b = 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return 'This is Student class.'

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, slice):
            return 'The item is not slice, is int!'
        c, d = 1, 1
        for x in range(item):
            c, d = d, c + d
        return c

    def __getattr__(self, item):
        if item == 'high':
            return '170'
        if item == 'weight':
            return lambda: 50
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self, *args, **kwargs):
        return 'This is a call method!'


s = Student('a', 18)
print(s.name)
print(s.age)
s.name = 'b'
print(s.name)
s.age = 60
print(s.age)
print(s)
for n in s:
    print(n)

print(s[10])
print(s[5:10])
print(s.high)
print(s.weight())
# print(s.fdfd)
print(s())
print(callable(s))


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().aaa.bbb.ccc.ddd)


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


def fn(self, name='world'):
    return 'Hello, %s.' % name


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))


def dic():
    """

    :return:
    """
    pass


print(os.name)
print(os.uname())

"""python 单利模式详细文档
    https://www.cnblogs.com/huchong/p/8244279.html
"""


def singleton(cls):

    _instance = {}

    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]

    return _singleton


@singleton
class A(object):

    def __init__(self, _name=0):
        self.name = _name


def task(arg):
    obj = A(arg)
    print(obj)


for i in range(10):
    # time.sleep(1)
    t = threading.Thread(target=task, args=[i])
    t.start()


class A(object):
    _instance_lock = threading.Lock()

    def __init__(self, _name=0):
        self.name = _name

    def __new__(cls, *args, **kwargs):
        if not hasattr(A, '_instance'):
            with A._instance_lock:
                if not hasattr(A, '_instance'):
                    A._instance = object.__new__(cls)
        return A._instance


def task(arg):
    obj = A(arg)
    print(obj)


for i in range(10):
    # time.sleep(1)
    t = threading.Thread(target=task, args=[i])
    t.start()

