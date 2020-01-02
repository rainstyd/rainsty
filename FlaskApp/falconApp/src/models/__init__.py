#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   __init__.py
@time:   2019-12-30 15:29:29
@description:
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from sqlalchemy import (
    create_engine, ForeignKey, Column, Integer, String, Text, DateTime, Date, Numeric, Time, and_, or_,
    SmallInteger, Float, DECIMAL, desc, asc, Table, join, event, extract, not_, case, func
)
from sqlalchemy.orm import relationships, backref, sessionmaker, scoped_session, aliased, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.sql import exists
from sqlalchemy.pool import NullPool
from src.config import AppConfig

DBBase = declarative_base()
db_engine = create_engine(AppConfig.sqlite_db_path, pool_recycle=7200, encoding='utf-8')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))
DBBase.query = db_session.query_property()


from src.models.user import *


if __name__ == '__main__':
    print('Update sqlite table structure...')
    try:
        DBBase.metadata.create_all(db_engine)

        user = db_session.query(User).filter(
            User.username == 'admin'
        ).first()
        if not user:
            db_session.add(User(**dict(username='admin', password='123456')))
            db_session.commit()
        print('update successful!')
    except BaseException as e:
        db_session.rollback()
        print(e)
        print('update failed!')
