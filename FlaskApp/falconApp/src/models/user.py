#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   user.py
@time:   2019-12-30 16:14:29
@description:
"""

from . import DBBase, Column, Integer, String


class User(DBBase):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(16), nullable=True)
    password = Column('password', String(16), nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        _dict = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return _dict
