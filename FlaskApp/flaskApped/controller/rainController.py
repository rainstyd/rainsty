# -*- coding: utf-8 -*-
import json
from flask import g, render_template, current_app
from module.rainModuleUser import rainModuleUser as User
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def rainEnrollment(self):
    RAINDB_CONF = current_app.config['RAINDB_CONF']
    username = self['username']
    password = self['password']
    user = User(username=username)
    result = user.query(RAINDB_CONF)

    if result is None:
        user = User(username=username, password=pwd_context.encrypt(password))
        res = user.save(RAINDB_CONF)
        if res is True:
            return json.dumps({"success": True, "result": "User registered success!"})
        else:
            return json.dumps({"success": False, "result": "Unknown exception!"})
    else:
        if username in json.dumps(result):
            return json.dumps({"success": False, "result": "User is already registered!"})
        else:
            return json.dumps({"success": False, "result": "Unknown exception!"})


def rainEntrance(self):
    RAINDB_CONF = current_app.config['RAINDB_CONF']
    username = self['username']
    password = self['password']
    user = User(username=username)
    result = user.query(RAINDB_CONF)

    if result is None:
        return json.dumps({"success": False})
    elif username in json.dumps(result):
        if pwd_context.verify(password, result['password']) is True:
            g.user = user
            try:
                expiration = 10
                token = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration).dumps({'username': username})
                return json.dumps({"success": True, "token": token.decode('ascii')})
            except BaseException as e:
                print(e)
                return json.dumps({"success": False})
    else:
        return json.dumps({"success": False})


def rainVerifyInfo(self):
    return render_template("entergoin.html", token=self['input_entergoin'])

