# -*- coding: utf-8 -*-


def logConf():
    conf = dict(
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='[%Y-%m-%d %H:%M:%S]',
        filename='./logs/rainLog.log',
        filemode='a'
    )
    return conf


def rainLog(*params):
    self = params[0]
    logging = params[1]
    error = params[2]
    return logging.error('%s %s %s' % (self.url, self.method, error))
