# -*- encoding: utf-8 -*-

"""
@author:  rainsty
@file:    pgsql_conn.py
@time:    2025-07-26 13:52:28
@version: v1.0.23
@description:

    1: postgresql连接类
        version: v1.0.24
        update:  2025-08-26 13:34:28
        desc:    更改类名

"""


import psycopg2


class PgsqlConnect(object):

    def __init__(self, _config, **kwargs):
        self.__config = _config
        self.__kwargs = kwargs
        self.__conn = None
        self.__cursor = None
        self.config = self.__config
        self.__config['port'] = int(self.__config['port'])

    @property
    def get_conn(self):
        return self.__conn

    @property
    def get_cursor(self):
        return self.__cursor

    def create_connect(self):
        self.__conn = psycopg2.connect(**self.__config, **self.__kwargs)
        self.__cursor = self.__conn.cursor()

    def check_connect(self):
        try:
            if self.__conn.closed != 0:
                raise psycopg2.Error('The connect is closed.')
        except (BaseException,):
            self.create_connect()

    def close_connect(self):
        try:
            if self.__cursor:
                self.__cursor.close()
            if self.__conn:
                self.__conn.close()
            self.__cursor = None
            self.__conn = None
            return True
        except (BaseException,):
            return False

    def __del__(self):
        self.close_connect()

    def get_data(self, sql, params=None):
        try:
            self.check_connect()
            if params:
                self.__cursor.execute(sql, params)
            else:
                self.__cursor.execute(sql)

            _data = self.__cursor.fetchall()
            _column = self.__cursor.description
            _result = [dict(zip([column[0] for column in _column], data)) for data in _data]
            self.__conn.commit()
            return _result
        except BaseException as _e:
            raise _e

    def exec_cmd(self, sql, params=None, autocommit=True):
        try:
            self.check_connect()
            if params:
                if isinstance(params, list):
                    self.__cursor.executemany(sql, params)
                else:
                    self.__cursor.execute(sql, params)
            else:
                self.__cursor.execute(sql)
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
