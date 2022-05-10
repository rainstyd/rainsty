# -*- coding: utf-8 -*-


import sys
import confluent_kafka
import datetime
from streamparse import Bolt


class PutKafka(Bolt):
    outputs = ["PutKafka"]

    def initialize(self, conf, context):
        self._init_param(conf)
        self._init_producer()

    def _init_param(self, conf):

        self.kafka_config = conf.get('kafka_config', {})
        self.topic_name = self.kafka_config.get('topic_name')
        self.partition = conf.get('partition', None)

    def _init_producer(self):

        try:
            msg = dict(topic_name=self.topic_name, partition=self.partition, kafka_config=self.kafka_config)
            self.logger.info(('PutKafka', '[_init_consumer:1001]', '开始创建生产者', sys._getframe().f_lineno, msg))

            kafka_config = {
                'bootstrap.servers': str(self.kafka_config.get('bootstrap_servers')),
                'message.max.bytes': int(self.kafka_config.get('message_max_bytes', '100000000'))
            }
            self.producer = confluent_kafka.Producer(kafka_config)

            msg = dict(topic_name=self.topic_name, partition=self.partition, kafka_config=kafka_config)
            self.logger.info(('PutKafka', '[_init_consumer:1002]', '创建生产者成功', sys._getframe().f_lineno, msg))

        except BaseException as e:
            msg = dict(errno=e.__traceback__.tb_lineno, errmsg=e)
            self.logger.error(('PutKafka', '[_init_consumer:1003]', '创建生产者异常', sys._getframe().f_lineno, msg))

    def on_delivery(self, err, msg):

        try:
            if err is not None:
                msg = dict(error=err, msg=msg.value())
                self.logger.error(('PutKafka', '[on_delivery:1001]', 'kafka回调异常', sys._getframe().f_lineno, msg))
            else:
                msg = dict(topic=msg.topic(), partition=msg.partition(), offset=msg.offset())
                self.logger.info(('PutKafka', '[on_delivery:1002]', 'kafka回调成功', sys._getframe().f_lineno, msg))
        except Exception as e:
            msg = dict(errno=e.__traceback__.tb_lineno, errmsg=e, msg=msg.values())
            self.logger.error(('PutKafka', '[on_delivery:1003]', 'kafka回调异常', sys._getframe().f_lineno, msg))

    def process_tick(self, tup):

        try:
            if datetime.datetime.now().second % 5 == 0:
                self.producer.flush()
                self.logger.info(('PutKafka', '[process_tick:1001]', 'flush推送成功', sys._getframe().f_lineno))

        except BaseException as e:
            msg = dict(errno=e.__traceback__.tb_lineno, errmsg=e)
            self.logger.error(('PutKafka', '[process_tick:1002]', 'flush推送异常', sys._getframe().f_lineno, msg))

    def process(self, tup):

        try:
            msg = tup.values[0]
            self.producer.poll(1)

            if not self.partition:
                self.producer.produce(topic=self.topic_name, value=msg.encode(), callback=self.on_delivery)
            else:
                self.producer.produce(topic=self.topic_name, value=msg.encode(), callback=self.on_delivery, partition=int(self.partition))

            # self.producer.flush()
            self.logger.info(msg.encode())
            self.emit([])
            return

        except Exception as e:
            msg = dict(errno=e.__traceback__.tb_lineno, errmsg=e, tup=tup)
            self.logger.error(('PutKafka', '[process:1001]', '数据发往kafka队列失败', sys._getframe().f_lineno, msg))
            self._init_producer()
            return

    def __del__(self):
        self.producer.flush()
