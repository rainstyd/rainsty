# -*- encoding: utf-8 -*-

"""
@author:  rainsty
@file:    mysql_conn.py
@time:    2025-07-26 13:52:28
@version: v1.0.23
@description:

    1: pymysql连接类
        version: v1.0.23
        update:  2025-07-26 13:52:28
        desc:    去掉 _column = cur.description

"""

import pymysql
from pymysql.cursors import DictCursor


class MysqlConnect(object):

    def __init__(self, _config, **kwargs):
        self.__config = _config
        self.__kwargs = kwargs
        self.__conn = None
        self.__cursor = None
        self.__config['port'] = int(self.__config['port'])
        self.__config['connect_timeout'] = int(self.__config.get('connect_timeout', 10))
        self.__config['cursorclass'] = DictCursor

    def get_conn(self):
        return self.__conn

    def get_cursor(self):
        return self.__conn.cursor()

    def create_connect(self):
        self.__conn = pymysql.Connection(**self.__config, **self.__kwargs)
        self.__cursor = self.__conn.cursor()

    def check_connect(self):
        try:
            self.__conn.ping()
        except (AttributeError,):
            self.create_connect()

    def close_connect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__conn:
            self.__conn.close()
        self.__cursor = None
        self.__conn = None

    def __del__(self):
        self.close_connect()

    def get_data(self, sql, params=None, autocommit=True):
        try:
            self.check_connect()
            with self.get_cursor() as cur:
                if params:
                    cur.execute(sql, params)
                else:
                    cur.execute(sql)
                _data = cur.fetchall()
                if autocommit:
                    self.__conn.commit()
                return _data
        except BaseException as _e:
            raise _e

    def exec_cmd(self, sql, params=None, autocommit=True):
        try:
            self.check_connect()
            with self.get_cursor() as cur:
                if params:
                    if isinstance(params, list):
                        cur.executemany(sql, params)
                    else:
                        cur.execute(sql, params)
                else:
                    cur.execute(sql)
                if autocommit:
                    self.__conn.commit()
                return True
        except BaseException as _e:
            if autocommit:
                self.__conn.rollback()
            raise _e

    def to_commit(self):
        try:
            self.__conn.commit()
        except BaseException as _e:
            self.__conn.rollback()
            raise _e
