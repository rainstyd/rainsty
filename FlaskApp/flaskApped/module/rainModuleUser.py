# -*- coding: UTF-8 -*-
import sys
sys.path.append('./lib')
from raindborm import Model
from raindborm import Column


class rainModuleUser(Model):

    username = Column('String', 'username', 255)
    password = Column('String', 'password', 255)
