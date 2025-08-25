# -*- encoding: utf-8 -*-

"""
@author:  rainsty
@file:    decorator.py
@time:    2020-08-17 09:04:29
@version: v1.0.22
@description:

    1: 功能号父类(DoActionExample)
        version: v1.0.22
        update:  2024-04-08 16:16:16
        desc:    去掉类中的日志实例

"""

import os
import json
import errno
import decimal
import logging
import datetime
import functools
import time
import copy

# try:
#     import sys
#     import codecs
#     sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# except BaseException as ei:
#     print('Stdout Error: '.format(ei))


class DoActionExample(object):

    def __init__(self):
        """ 全局标识
        """
        self.mark = '|'
        self.sign = '\r\n'
        self.index = 'INDEX'
        self.number = 'ErrorNo'
        self.message = 'ErrorMessage'
        self.line = 'ErrorLine'
        self.reason = 'ErrorReason'
        self.params = {}
        self.initialize()

    def initialize(self):
        """ 初始化功能号: 默认参数/返回值/默认配置
        """
        self._init_params()
        self._init_result()
        self._init_config()

    def _init_params(self):
        """ 默认参数
        """
        pass

    def _init_result(self):
        """ 返回值
        """
        pass

    def _init_config(self):
        """ 默认配置
        """
        pass

    def result_list(self, ans, name, index=True, index_key=True, data=None, key=None, key_index=None):
        """ GRID数组返回
            usage: self._result_list(ans, 'GRID0', data=data, key=self.key_1001)
            index: 是否需要数组索引
            data: 数组包字典
            index_key: 是否需要数组索引前缀，self.index
            key_index: 返回的索引名称更改内容，对应key
        """
        if not data or len(data) == 0:
            ans[self.number] = 0
            ans[self.message] = '未能找到信息'
            return

        data = [self.clean_none(dict(i)) for i in data]

        result = [self.mark.join(str(dict(d).get(k, '')) for k in key) for d in data]
        result = self.sign.join(result)

        ans[name] = result

        if key_index:
            self.index_list(ans, index=index, index_key=index_key, key=key_index)
        else:
            self.index_list(ans, index=index, index_key=index_key, key=key)

        ans[self.number] = len(data)
        ans[self.message] = '成功'
        return

    def result_json(self, ans, data=None, key=None, key_index=None):
        """ JSON返回
            data: json或者数组,字典
            usage: self._result_json(ans, data=data, key=self.key_1001)
        """
        if not data or len(data) == 0:
            ans[self.number] = 0
            ans[self.message] = '未能找到信息'
            return

        if key_index:
            name = key_index[0]
        else:
            name = key[0]

        if isinstance(data, dict):
            ans[name] = json.dumps(data, ensure_ascii=False)
        elif isinstance(data, list):
            data = [dict(d) for d in data]
            ans[name] = json.dumps(data, ensure_ascii=False)
        elif isinstance(data, str):
            ans[name] = data
        else:
            ans[name] = data

        ans[self.number] = len(data)
        ans[self.message] = '成功'
        return

    def result_key_value(self, ans, data=None, key=None, key_index=None):
        """ 键值对返回
            data: 字典或者数组
            usage: self._result_key_value(ans, data=data, key=self.key_1001)
        """
        if not data or len(data) == 0:
            ans[self.number] = 0
            ans[self.message] = '未能找到信息'
            return

        if isinstance(data, list):
            data = data[0]

        data = self.clean_none(dict(data))

        if key_index:
            for i in range(len(key)):
                try:
                    ans[key_index[i]] = data.get(key[i], '')
                except (BaseException,):
                    ans[key_index[i]] = ''
        else:
            for i in range(len(key)):
                try:
                    ans[key[i]] = data.get(key[i], '')
                except (BaseException,):
                    ans[key[i]] = ''

        ans[self.number] = len(data)
        ans[self.message] = '成功'
        return

    def index_list(self, ans, index=True, index_key=True, key=None):
        """ 数组返回使用的索引
        """
        if index:
            for ki in range(len(key)):
                if not index_key:
                    ans['{}'.format(key[ki])] = ki
                else:
                    ans['{}_{}'.format(self.index, key[ki])] = ki
        return

    @staticmethod
    def clean_none(d):
        """ 清理None数据，格式化时间，格式化DECIMAL
        """
        for k, v in d.items():
            if v is None:
                d[k] = ''
            if isinstance(v, decimal.Decimal):
                d[k] = str('%.6f' % float(v))

            if isinstance(v, datetime.datetime):
                d[k] = v.strftime("%Y-%m-%d %H:%M:%S")
            if isinstance(v, int):
                d[k] = str(v)
            if isinstance(v, float):
                d[k] = str('%.6f' % v)
        return d

    def check_params(self, req, ans, check_dict, error_code=-2601):
        """ 参数检查
        """
        check_result, check_error = self.check_params_type(req, check_dict)

        if not check_result:
            ans[self.message] = check_error
            ans[self.number] = error_code
            return False
        else:
            return True

    @staticmethod
    def check_params_type(request, check_dict):
        """ 参数检查-类型检查
        """
        try:
            for k, v in check_dict.items():
                if not request[k]:
                    return False, '[{}]不能为空'.format(k)
                try:
                    if v == 'int':
                        int(request[k])

                    if v == 'str':
                        str(request[k])

                    if isinstance(v, list):
                        if request[k] not in v:
                            return False, '[{}]业务类型错误, 应该包含在{}里面'.format(k, v)

                except BaseException as e1:
                    return False, '[{}]类型错误, 应该为: {};  Error: {}'.format(k, v, e1)

            return True, None
        except BaseException as e2:
            return False, e2

    @staticmethod
    def trans_req(req):
        if not isinstance(req, dict):
            req_dict = {k: v.decode() for k, v in req.dict.items() if isinstance(v, bytes)}
            req_dict.update({k: v for k, v in req.dict.items() if not isinstance(v, bytes)})
        else:
            req_dict = copy.deepcopy(req)
        return req_dict

    def get_doc(self, req, ans):

        doc = """
        action_name
        action_desc
        
        ---
        
        tags:
        
          - action_tags
          
        parameters:
          {}
          
        responses:
          200:
            schema:
              properties:
              
                errorno:
                  type: string
                  description:
                  default:

                errormessage:
                  type: string
                  description:
                  default:
                {}
        """

        req_key_list_default = ['gatewayport', 'action', 'tfrom', 'handleserialno', 'gatewayip']
        req_key = [k for k in req.dict.keys() if k not in req_key_list_default]
        req_key = ["""
          - name: {}
            in: query
            type: string
            required: 
            description: """.format(k) for k in req_key]
        req_key = '\r\n'.join(req_key)
        ans_key_list_default = [self.number.lower(), self.message.lower()]
        ans_key = ["""
                {}:
                  type: string
                  description: 
                  default: """.format(k) for k in ans.dict.keys() if k not in ans_key_list_default]
        ans_key = '\r\n'.join(ans_key)

        doc = doc.format(req_key, ans_key)
        print(doc)

    def get_doc_auto(self, req, ans, name, desc, tag, params, keys):

        doc = """
        {}
        {}

        ---

        tags:

          - {}

        parameters:
          {}

        responses:
          200:
            schema:
              properties:

                errorno:
                  type: string
                  description: 错误号(条数)
                  default:

                errormessage:
                  type: string
                  description: 错误信息
                  default:
                {}
        """

        keys_dict = dict()
        for d in keys:
            keys_dict[d['index']] = d

        # req_key_list_default = ['gatewayport', 'action', 'tfrom', 'handleserialno', 'gatewayip']
        req_key_list_default = list(params.keys())
        # req_key = [k for k in req.dict.keys() if k not in req_key_list_default]
        req_key = [k for k in req.dict.keys() if k in req_key_list_default]
        req_key = ["""
          - name: {}
            in: query
            type: string
            required: 
            description: {}""".format(k, params.get(k, {}).get('desc', '')) for k in req_key]
        req_key = '\r\n'.join(req_key)
        ans_key_list_default = [self.number.lower(), self.message.lower()]
        ans_key = ["""
                {}:
                  type: string
                  description: {}
                  default: """.format(k, keys_dict.get(k, {}).get('desc', '')) for k in ans.dict.keys() if
                   k not in ans_key_list_default]
        ans_key = '\r\n'.join(ans_key)

        doc = doc.format(name, desc, tag, req_key, ans_key)
        print(doc)

    @staticmethod
    def handle_params(params):

        _params = dict()
        for k in params.keys():
            _params[k] = params[k]['key']

        return _params
    
    def do_action(self, req, ans, inf):
        print(self.params, req, ans, inf)
        return ans

    def test_interface(self, req_debug):

        class Inf(object):

            def __init__(self):
                self.threadtag = 0

        inf_debug = Inf()
        ans_debug = dict()

        self.do_action(req_debug, ans_debug, inf_debug)
        return ans_debug

    @staticmethod
    def analyse_action(do_test):
        print('#', do_test.action_code, do_test.action_name, do_test.action_version)

    @staticmethod
    def analyse_ans(req_test, ans_test, do_test, params, params_name):
        print('##', '{}-{}-{}'.format(do_test.action_code, req_test.get('menu_id', ''),
                                      do_test.menu_id.get(req_test.get('menu_id', ''), '')))
        print('###', '请求参数')
        print('|参数|类型|说明|')
        print('|---|---|---|')
        for k, v in req_test.items():
            print('|{}|{}|{}|'.format(k, str(type(v))[8:-2],
                                      do_test.menu_id.get(v, '') if k == 'menu_id' else params_name.get(k, '')))
            params.add(k)

        print('###', '应答内容')
        print('|一级字段|二级字段|三级字段|说明|')
        print('|---|---|---|---|')
        for k, v in ans_test.items():
            print('|{}| | |{}|'.format(k, params_name.get(k, '')))
            try:
                v = json.loads(v)
                if isinstance(v, list):
                    try:
                        v1 = v[0]
                        for k1 in v1.keys():
                            print('| |{}| |{}|'.format(k1, params_name.get(k1, '')))
                            params.add(k1)
                            if isinstance(v1[k1], list):
                                try:
                                    v2 = v1[k1][0]
                                    for k2 in v2.keys():
                                        print('| | |{}|{}|'.format(k2, params_name.get(k2, '')))
                                        params.add(k2)
                                except (BaseException,):
                                    pass
                    except (BaseException,):
                        pass
                elif isinstance(v, dict):
                    for k1 in v.keys():
                        print('| |{}| |{}|'.format(k1, params_name.get(k1, '')))
                        params.add(k1)
                        if isinstance(v[k1], list):
                            try:
                                v1 = v[k1][0]
                                for k2 in v1.keys():
                                    print('| | |{}|{}|'.format(k2, params_name.get(k2, '')))
                                    params.add(k2)
                            except (BaseException,):
                                pass

            except (BaseException,):
                pass

        print('###', '样例数据：')
        print('```')
        data = ans_test.get('data')
        data = json.loads(data)
        if isinstance(data, list):
            data = data[:3]
        print(json.dumps(data, indent=4, ensure_ascii=False))
        print('```')

        return params


class MidnightRotatingFileHandler(logging.FileHandler):

    def __init__(self, filename):
        self._filename = filename
        self._rotate_at = self._next_rotate_datetime()
        super(MidnightRotatingFileHandler, self).__init__(filename, mode='a')

    @staticmethod
    def _next_rotate_datetime():
        now = datetime.datetime.now()
        return now.replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)

    def _open(self):
        now = datetime.datetime.now()
        log_today = "%s.%s" % (self._filename, now.strftime('%Y-%m-%d'))
        try:
            fd = os.open(log_today, os.O_CREAT | os.O_EXCL)
            os.close(fd)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.baseFilename = log_today
        return super(MidnightRotatingFileHandler, self)._open()

    def emit(self, record):
        now = datetime.datetime.now()
        if now > self._rotate_at:
            self._rotate_at = self._next_rotate_datetime()
            self.close()
        super(MidnightRotatingFileHandler, self).emit(record)


class Logger(object):

    def __init__(self, base_path, log_dir_name, log_file_name, log_format=None):

        self.__base_path = base_path
        self.__log_dir_name = log_dir_name
        self.__log_file_name = log_file_name
        self.__logger = None
        self.__log_format = log_format
        self.__logger_self = None
        self.filename = os.path.join(self.__base_path, self.__log_dir_name, self.__log_file_name)

    def get_logger(self):
        if self.__logger_self:
            return self.__logger_self
        else:
            if not self.__logger:
                self.__logger = logging.getLogger(__name__)
            log_format = '[%(asctime)s] %(levelname)s %(pathname)s:%(lineno)d %(message)s'

            self.__logger.setLevel(logging.INFO)
            self.__log_format = self.__log_format if self.__log_format else log_format

            log_dir_path = os.path.join(self.__base_path, self.__log_dir_name)
            if not os.path.exists(log_dir_path):
                os.makedirs(log_dir_path)

            log_file_folder = os.path.join(log_dir_path, self.__log_file_name)
            file_log_handler = MidnightRotatingFileHandler(log_file_folder)

            formatter = logging.Formatter(self.__log_format)
            file_log_handler.setFormatter(formatter)
            self.__logger.addHandler(file_log_handler)
            self.__logger_self = self.__logger
            return self.__logger_self


def action(action_code, action_name, action_version, file=__file__):
    def f(func):
        @functools.wraps(func)
        def w(*args, **kwargs):
            # print('call %s(): the param is %s.' % (func.__name__, file))
            return func(*args, **kwargs)
        return w
    return f


class ActionTest(object):

    def __init__(self):

        class Inf(object):
            threadtag = 0

        self.req = dict()
        self.ans = dict()
        self.inf = Inf()


def action_test(req, ans, inf):
    try:
        print('=' * 24 + '请求' + '=' * 48)
        print(json.dumps(req, indent=2, ensure_ascii=False))
        print('=' * 24 + '应答' + '=' * 48)
        print(json.dumps(ans, indent=2, ensure_ascii=False))
    except BaseException as e:
        print(__file__, e.__traceback__.tb_lineno, e)


def to_request(_action, params):
    print('*' * 120)
    start = time.time()
    test = ActionTest()
    print('# project请求参数: ')
    print(params.strip())
    print()
    print('# postman请求参数:')
    print(params.replace('=', ':').strip())
    print()
    params = [p.strip().split('=', 1) for p in params.split('\n') if p.strip() != '']
    for p in params:
        test.req[p[0]] = p[1]
    print('# python请求参数:')
    params = copy.deepcopy(test.req)
    print(params)
    print()
    print('# 以下为程序代码的打印:', '*' * 100)
    _action(test.req, test.ans, test.inf)
    action_test(test.req, test.ans, test.inf)
    print(time.time() - start)
