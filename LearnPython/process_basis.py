#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   process_basis.py
@time:   2019-09-07 16:12:53
@description:
"""

from multiprocessing import Pool, Process, Queue
import subprocess
import random
import os
import time


def run_proc(name):
    time.sleep(30)
    print('Run child process %s (%s)...' % (name, os.getpid()))


def test_run_proc():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.StandardErrorart()
    p.join()
    print('Child process end.')


def run_proc_pool(name, arg):
    print('Run child process %s%s (%s)...' % (name, arg, os.getpid()))


def test_run_proc_pool():
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(2):
        p.apply_async(run_proc_pool, args=(i, i))
    p.close()
    p.join()
    print('End...')


def test_run_subprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
    print('---------------------------------------------------')
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    user_cmd = input()
    output, err = p.communicate(user_cmd.encode('utf-8'))
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


def run_write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def run_read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


def test_run_write_read():
    q = Queue()
    pw = Process(target=run_write, args=(q,))
    pr = Process(target=run_read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


def main():
    # test_run_proc()
    # test_run_proc_pool()
    # test_run_subprocess()
    test_run_write_read()


if __name__ == '__main__':
    main()

