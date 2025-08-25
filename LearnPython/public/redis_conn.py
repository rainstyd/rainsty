# -*- encoding: utf-8 -*-

"""
@author:  rainsty
@file:    redis_conn.py
@time:    2025-07-26 13:52:28
@version: v1.0.23
@description:

    1: redis连接类
        version: v1.0.23
        update:  2025-07-26 13:52:28
        desc:    新增说明

"""

import datetime
import redis
from redis.sentinel import Sentinel
from rediscluster import RedisCluster


class RedisConnect(object):
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.ADDRESS = config.get('host')
        self.PORTS = config.get('port')
        self.REDIS_DB = config.get('db')
        self.REDIS_PASSWORD = config.get('password')
        self.master = None
        self.slave = None
        self.master_conn = None
        self.slave_conn = None
        self.single_pool = None
        self.master_pool = None
        self.slave_pool = None
        self.cluster_conn = None
        self.startup_nodes = None
        self.sentinel = None
        self.mastername = config.get('mastername', 'mymaster')

    # -------------------- 主从+哨兵 开始 --------------------
    def sentinel_conn(self):
        # 连接哨兵服务器
        ADDRESS = self.ADDRESS.split(',')
        PORTS = self.PORTS.split(',')
        sentiel_servers = [(ADDRESS[x], int(PORTS[x])) for x in range(ADDRESS.__len__())]
        self.sentinel = Sentinel(sentiel_servers, socket_connect_timeout=10)
        # 获取主服务器地址
        self.master = self.sentinel.discover_master(self.mastername)
        self.logger.info("主服务器地址:{}".format(self.master))
        # 获取从服务器地址
        self.slave = self.sentinel.discover_slaves(self.mastername)
        self.logger.info("从服务器地址:{}".format(self.slave))

    def make_master_conn(self):
        self.logger.info("注意:连接的是主从哨兵的主节点")
        _config = dict(
            host=self.master[0],
            port=self.master[1],
            db=self.REDIS_DB,
            password=self.REDIS_PASSWORD,
            socket_connect_timeout=10
        )
        self.master_pool = redis.ConnectionPool(**_config)
        self.master_conn = redis.Redis(connection_pool=self.master_pool)

    def make_slave_conn(self):
        self.logger.info("注意:连接的是主从哨兵的从节点")
        _config = dict(
            host=self.slave[0][0],
            port=self.slave[0][1],
            db=self.REDIS_DB,
            password=self.REDIS_PASSWORD,
            socket_connect_timeout=10
        )
        self.slave_pool = redis.ConnectionPool(**_config)
        self.slave_conn = redis.Redis(connection_pool=self.slave_pool)

    def get_cursor(self, identity, check='select'):
        cursor = None
        if identity == 'master':
            try:
                if self.master_conn:
                    if check == 'insert':
                        self.master_conn.zadd("keep_live", {'get_cursor': datetime.datetime.now().strftime("%Y%m%d%H%M%S")})
                        self.logger.info('start check insert')
                        cursor = self.master_conn
                    elif check == 'select':
                        self.logger.info('start check select')
                        if self.master_conn.ping():
                            cursor = self.master_conn
                        else:
                            raise redis.exceptions.RedisError
                else:
                    self.sentinel_conn()
                    self.make_master_conn()
                    cursor = self.master_conn
            except redis.exceptions.RedisError:
                self.logger.info("主从:redis数据库连接尝试失败...")
                # time.sleep(10)
                self.sentinel_conn()
                self.make_master_conn()
                cursor = self.master_conn
            except Exception as e:
                self.logger.info("主从:redis数据库连接失败,其它异常:{}...".format(e))
        elif identity == 'slave':
            try:
                if self.slave_conn:
                    if self.slave_conn.ping():
                        cursor = self.slave_conn
                    else:
                        raise redis.exceptions.RedisError
                else:
                    self.sentinel_conn()
                    self.make_slave_conn()
                    cursor = self.slave_conn
            except redis.exceptions.RedisError:
                self.logger.info("主从:redis数据库连接尝试失败...")
                # time.sleep(10)
                self.sentinel_conn()
                self.make_slave_conn()
                cursor = self.slave_conn
            except Exception as e:
                self.logger.info("主从:redis数据库连接失败,其它异常:{}...".format(e))
        return cursor

    # 主从模式
    def deal_sql_ms(self, identity, check):
        # try:
        cursor = self.get_cursor(identity, check)
        return cursor

    # -------------------- 主从+哨兵 结束 --------------------

    # -------------------- 单点 开始 --------------------
    # 单点模式
    def single_conn(self):
        cursor = None
        _config = dict(
            host=self.ADDRESS,
            port=int(self.PORTS),
            db=self.REDIS_DB,
            password=self.REDIS_PASSWORD,
            socket_connect_timeout=10
        )
        if self.single_pool:
            try:
                cursor = redis.StrictRedis(connection_pool=self.single_pool)
            except (Exception,):
                try:
                    self.single_pool = redis.ConnectionPool(**_config)
                    cursor = redis.StrictRedis(connection_pool=self.single_pool)
                    cursor.ping()
                except (Exception,):
                    self.logger.info("单点:redis数据库连接失败...")
        else:
            try:
                self.single_pool = redis.ConnectionPool(**_config)
                cursor = redis.StrictRedis(connection_pool=self.single_pool)
                cursor.ping()
            except (Exception,):
                self.logger.info("单点:redis数据库连接失败...")
                # raise ApiError(-100, "单点:redis数据库连接失败...")
        return cursor

    # 单点模式
    def deal_sql_sp(self):
        cursor = self.single_conn()
        return cursor

    # -------------------- 单点 结束 --------------------

    # -------------------- 集群 开始 --------------------
    def make_cluster_conn(self):
        # 连接集群服务器
        ADDRESS = self.ADDRESS.split(',')
        PORTS = self.PORTS.split(',')
        nodes_len = ADDRESS.__len__()
        self.startup_nodes = [{"host": ADDRESS[x], "port": PORTS[x]} for x in range(nodes_len)]
        self.logger.info("集群节点服务器地址:{}".format(self.startup_nodes))
        _config = dict(startup_nodes=self.startup_nodes, password=self.REDIS_PASSWORD, socket_connect_timeout=10)
        self.cluster_conn = RedisCluster(**_config)

    def get_cluster_cursor(self, check='select'):
        cursor = None
        try:
            if self.cluster_conn:
                if check == 'insert':
                    self.logger.info('start check insert')
                    if self.cluster_conn.ping():
                        cursor = self.cluster_conn
                    else:
                        raise redis.exceptions.RedisError
                elif check == 'select':
                    self.logger.info('start check select')
                    if self.cluster_conn.ping():
                        cursor = self.cluster_conn
                    else:
                        raise redis.exceptions.RedisError
            else:
                self.make_cluster_conn()
                cursor = self.cluster_conn
        except redis.exceptions.RedisError:
            self.logger.info("集群:redis数据库连接失败,10s后重连一次...")
            # time.sleep(10)
            self.make_cluster_conn()
            cursor = self.cluster_conn
        except Exception as e:
            self.logger.info("集群:redis数据库连接失败,其它异常:{}...".format(e))
        finally:
            return cursor

    # 集群模式
    def deal_sql_cluster(self, check):
        cursor = self.get_cluster_cursor(check)
        return cursor

    # -------------------- 集群 结束 --------------------

    def get_redis_conn(self, identity='master', check='select'):

        try:
            redis_mode = self.config.get('mode', '0')
        except (BaseException,):
            redis_mode = '0'
        if redis_mode == '0':
            return self.deal_sql_sp()
        elif redis_mode == '1':
            return self.deal_sql_ms(identity, check)
        elif redis_mode == '2':
            return self.deal_sql_cluster(check)

    def create_connect(self):
        self.get_redis_conn(check='insert')
