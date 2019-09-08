#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   thread_basis.py
@time:   2019-09-07 17:47:27
@description:
"""

import time
import threading

balance = 0
lock = threading.Lock()
local_school = threading.local()


def run_loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def test_run_loop():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run_loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


# def run_thread(n):
#     for i in range(100):
#         change_it(n)


def run_thread(n):
    for i in range(100):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def test_run_thread():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


def run_process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def run_process_thread(name):
    local_school.student = name
    run_process_student()


def test_run_thread_local():
    t1 = threading.Thread(target=run_process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=run_process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def main():
    print('test_run_loop---------------------')
    test_run_loop()
    print('test_run_thread----------------------')
    test_run_thread()
    print('test_run_thread_local--------------------')
    test_run_thread_local()


if __name__ == '__main__':
    main()

