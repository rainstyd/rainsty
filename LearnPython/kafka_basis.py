#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:  kafka_basis.py
@time:   2019-09-23 13:51:38
@description:
"""

import pykafka
from kafka import KafkaConsumer
from pykafka import KafkaClient
from datetime import datetime
import json

host = '127.0.0.1'


def get_topic():
    client = KafkaClient(hosts='{}:9192,{}:9193'.format(host, host))
    print(client.topics)
    topic = client.topics['rainsty']
    print(topic)


def get_message():
    consumer = KafkaConsumer(
        'rainsty',
        group_id='rainsty_0001',
        auto_offset_reset='earliest',
        bootstrap_servers=['{}:9192'.format(host), '{}:9193'.format(host)]
    )
    for message in consumer:
        try:
            message = json.loads(message.value.decode('utf-8'))
            print(message)
        except BaseException as e:
            print('{}: {}'.format(datetime.now(), e))
            continue

def main():
    get_topic()
    get_message()


if __name__ == '__main__':
    main()

