#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   test.py
@time:   2019-07-19 11:12
@description:
"""

# import asyncio
#
# def main():
#     numbers = [10, 3, 40, 8, 12]
#     for i in range(1, len(numbers)):
#         for j in range(0, len(numbers) - i):
#             # print(numbers)
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
#     print(numbers)
#
#
# main()
#
# # asyncio.ensureFuture()
#

# import asyncio
# from datetime import datetime
#
#
# @asyncio.coroutine
# def adjust_time(device, now):
#     yield from asyncio.ensureFuture(adjustTime(device, now))  # 下发校时指令
#
#
# loop = asyncio.get_event_loop()
# now = datetime.now()
# tasks = [adjust_time(device, now) for device in davices]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#
#
# import asyncio
#
#
# @asyncio.coroutine
# def wget_url(host):
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     pass
#
#
# urls = ['http://www.baidu.com/', 'http://www.163.com/', 'http://www.bing.com']
# loop = asyncio.get_event_loop()
# tasks = [wget_url(host) for host in urls]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#
#
# import asyncio
# import aiohttp
#
#
# async def get_url(url: str) ->str:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, timeout=10, verify_ssl=False) as r:
#             return await r.text()
#
#
# loop = asyncio.get_event_loop()
# tasks = [get_url(url) for url in urls]
# loop.run_until_complete(asyncio.wait(tasks))
#
# loop.close()
#
# import asyncio
# import aiohttp
#
#
# async def get_url(url: str) ->str:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, timeout=10, verify_ssl=False) as r:
#             return await r.text()
#
#
# loop = asyncio.get_event_loop()
# for url in urls:
#     loop.run_until_complete(get_url(url))
#
# loop.close()


class BinaryTree(object):
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):

        if self.leftChild == None:
            self.leftChild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, item):

        if self.rightChild == None:
            self.rightChild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.rightChild = self.rightChild
            self.rightChild = t


def build_tree_with_post(exp):
    stack = []
    oper = '+-*/'
    exp = exp[1:]
    for i in exp:
        if i not in oper:
            tree = BinaryTree(int(i))
            stack.append(tree)
        else:
            righttree = stack.pop()
            lefttree = stack.pop()
            tree = BinaryTree(i)
            tree.leftChild = lefttree
            tree.rightChild = righttree
            stack.append(tree)
    return stack.pop()

a = build_tree_with_post('(1+2)+(5*6-7)+3/4')
print(a)