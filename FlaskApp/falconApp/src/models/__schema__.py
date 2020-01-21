#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   __schema__.py
@time:   2020-01-21 16:50:29
@description: 初始化表结构
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from src.models import db_session, db_engine


if __name__ == '__main__':
    print('Update sqlite table structure...')
    try:
        from src.models.user import User, DBBase
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
