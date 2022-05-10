# -*- coding: utf-8 -*-


import sys
import uuid
import datetime
import confluent_kafka
from streamparse import Spout


class GetKafka(Spout):
    outputs = ["GetKafka"]

    def initialize(self, conf, context):

        self._init_param(conf)
        self._init_consumer()

    def _init_param(self, conf):

        self.kafka_config = conf.get('kafka_config', {})
        self.topic_name = self.kafka_config.get('topic_name')
        self.partition = conf.get('partition', None)
        self.group_id = self.kafka_config.get('group_id', uuid.uuid4().__str__())

    def _init_consumer(self):

        try:
            msg = dict(group_id=self.group_id, topic_name=self.topic_name, partition=self.partition, kafka_config=self.kafka_config)
            self.logger.info(('GetKafka', '[_init_consumer:1001]', '开始创建消费者', sys._getframe().f_lineno, msg))
            
            kafka_config = {
                'bootstrap.servers': str(self.kafka_config.get('bootstrap_servers')),
                'group.id': self.group_id,
                'default.topic.config': {
                    'enable.auto.commit': eval(self.kafka_config.get('enable_auto_commit', 'False')),
                    'auto.offset.reset': str(self.kafka_config.get('auto_offset_reset', 'latest')),
                    'auto.commit.interval.ms': int(self.kafka_config.get('auto_commit_interval_ms', '5000')),
                    'fetch.wait.max.ms': int((self.kafka_config.get('fetch_wait_max_ms', '5000')))
                }
            }
            self.consumer = confluent_kafka.Consumer(kafka_config)
            if not self.partition:
                self.consumer.subscribe(topics=[self.topic_name])
            else:
                self.consumer.assign([confluent_kafka.TopicPartition(topic=self.topic_name, partition=int(self.partition))])
            
            msg = dict(group_id=self.group_id, topic_name=self.topic_name, partition=self.partition, kafka_config=kafka_config)
            self.logger.info(('GetKafka', '[_init_consumer:1002]', '创建消费者成功', sys._getframe().f_lineno, msg))

        except BaseException as e:
            msg = dict(errno=e.__traceback__.tb_lineno, errmsg=e)
            self.logger.error(('GetKafka', '[_init_consumer:1003]', '创建消费者异常', sys._getframe().f_lineno, msg))

    def next_tuple(self):

        try:
            msg = self.consumer.poll(1)

            if msg is None:
                return

            if msg.error():
                if msg.error().code() == -191:
                    msg = dict(errmsg='msg.error(): -191.')
                    self.logger.error(('GetKafka', '[next_tuple:1001]', '消费者读取错误', sys._getframe().f_lineno, msg))
                    return
                else:
                    msg = dict(errmsg='msg.error(): other')
                    self.logger.error(('GetKafka', '[next_tuple:1002]', '消费者读取错误', sys._getframe().f_lineno, msg))
                    return
            
            self.logger.info(msg.value())
            self.emit([msg.value()])
            # self.consumer.commit()
            return

        except BaseException as e:
            msg = dict(errno=e.__traceback__.tb_lineno, errmsg=e)
            self.logger.error(('GetKafka', '[next_tuple:1003]', '消费者读取错误', sys._getframe().f_lineno, msg))
            self._init_consumer()
            return
