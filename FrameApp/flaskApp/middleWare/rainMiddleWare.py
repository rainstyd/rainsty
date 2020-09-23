# -*- coding: utf-8 -*-
import json
from functools import wraps
from flask import render_template, abort
from flask import redirect, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config.rainConfig import rainLog
import wrapt


def rainEnrollmentMW(self):
    def enrollmentMW(func):
        @wraps(func)
        def mw(*args, **kw):
            try:
                data = self.json
                username = data['username']
                password = data['password']
                if username == '' or username is None or password == '' or password is None:
                    return json.dumps({"success": False, "result": "User or pass cannot be empty!"})
            except BaseException as e:
                rainLog(self, current_app.logger, e)
                return abort(404)
            return func(*args, **kw)
        return mw
    return enrollmentMW


class rainEntranceMW(object):
    def __init__(self, request):
        self.request = request

    def __call__(self, func):
        @wraps(func)
        def mw(*args, **kw):
            try:
                if self.request.method == 'GET':
                    return render_template("entrance.html")
                elif self.request.method == 'POST':
                    form = self.request.form.to_dict()
                    username = form['username']
                    password = form['password']
                    if username == '' or username is None or password == '' or password is None:
                        return json.dumps({"success": False})
            except Exception as e:
                rainLog(self.request, current_app.logger, e)
                return abort(404)
            return func(*args, **kw)
        return mw


def rainEntergoinMW(self, form):
    @wrapt.decorator()
    def mw(func, instance, args, kwargs):
            def _requestTokenVerify(token):
                s = Serializer(current_app.config['SECRET_KEY'])
                try:
                    s.loads(token)
                    return True
                except BaseException as error:
                    rainLog(self, current_app.logger, error)
                    return False
            try:
                if self.method == 'GET':
                    return redirect('/rain')
                elif self.method == 'POST':
                    result = _requestTokenVerify(self.form.to_dict()['%s' % form])
                    if result is False:
                        return redirect('/rain')
            except Exception as e:
                rainLog(self, current_app.logger, e)
                return abort(404)
            return func(*args, **kwargs)
    return mw
