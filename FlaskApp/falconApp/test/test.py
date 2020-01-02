#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   test.py
@time:   2019-12-30 16:30:29
@description:
"""

from pyrainsty.iftest import InterfaceTest

test_host = '127.0.0.1'
test_port = 5000
version = 'v0.0.1'


class APITest(InterfaceTest):

    def test_main_get(self, path='/test/main'):
        payload = dict(
            username='admin',
            password='123456'
        )
        return self.get_request(path=path, payload=payload, title='主页')

    def test_main_post(self, path='/test/main'):
        payload = dict(
            username='admin',
            password='123456'
        )
        return self.post_request(path=path, payload=payload, title='主页')


if __name__ == '__main__':
    api = APITest('http://{}:{}/api/'.format(test_host, test_port), version)

    # test
    # api.test_login()
    api.test_main_get()
    api.test_main_post()
