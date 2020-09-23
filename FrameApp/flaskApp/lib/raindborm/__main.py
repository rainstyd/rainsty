# -*- coding: UTF-8 -*-
import os
import re
import json


def _getInfo(self, config):
    path = config['path']
    database = config['database']
    table = self.__table__
    fields = []
    args = []
    for k, v in self.__mappings__.items():
        fields.append(v.name)
        args.append(getattr(self, k, None))
    res = re.sub('{|}| |\"', '', json.dumps(dict(zip(fields, args))))
    res = re.sub(':', '==', res)
    res = res.replace('$', '\\$')
    return path, database, table, res


class _ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, _Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=_ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self, config):
        path, database, table, res = _getInfo(self, config)
        try:
            res = os.popen('cd %s; ./bin/rainDB-shell save %s %s %s' % (path, database, table, res)).read()
            if res == 'True':
                return True
            else:
                return False
        except BaseException as e:
            raise ValueError('ValueError: %s.' % e)

    def delete(self, config):
        path, database, table, res = _getInfo(self, config)
        try:
            res = os.popen('cd %s; ./bin/rainDB-shell delete %s %s %s' % (path, database, table, res)).read()
            if res == 'True':
                return True
            else:
                return False
        except BaseException as e:
            raise ValueError('ValueError: %s.' % e)

    def update(self, config):
        pass

    def query(self, config):
        path, database, table, res = _getInfo(self, config)
        res = res.split(',')
        res = [l for l in res if l.split('==')[1] != 'null']
        res = ",".join(res)
        try:
            res = os.popen('cd %s; ./bin/rainDB-shell query %s %s %s' % (path, database, table, res)).read()
            if res == 'None':
                return None
            else:
                d = {}
                for r in res.split(','):
                    d['%s' % r.split('==')[0]] = str(r.split('==')[1])
                return d
        except BaseException as e:
            raise ValueError('ValueError: %s.' % e)


class _Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class Column(_Field):
    __slots__ = ('name', 'type', 'len')

    def __init__(self, *args):
        self.type = args[0]
        self.name = args[1]
        self.len = args[2]

    def __getattr__(self):
        if self.type_name == 'String':
            super(Column, self).__init__(self.name, 'varchar(%s)' % self.len)
        elif self.type_name == 'Integer':
            super(Column, self).__init__(self.name, 'int(%s)' % self.len)
        else:
            raise AttributeError(r"'Model' object has no attribute '%s'" % self.type)
