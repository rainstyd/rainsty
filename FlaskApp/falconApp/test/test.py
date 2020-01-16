#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   test.py
@time:   2019-12-30 16:30:29
@description:
"""

from pyrainsty.iftest import InterfaceTest

"""
source activate rainsty
gunicorn -w 1 manage_app:app -b 0.0.0.0:5000 --timeout 1800
"""


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
    test_host = '127.0.0.1'
    test_port = 5000
    version = 'v0.0.1'

    api = APITest('http://{}:{}/api/'.format(test_host, test_port), version, is_login=True)

    api.test_main_get()
    api.test_main_post()
