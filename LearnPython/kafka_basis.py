#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   test_kafka.py
@time:   2019-11-01 09:52:29
@description:
"""

from kafka import KafkaConsumer
from pykafka import KafkaClient
from datetime import datetime
import json

host = '47.99.139.144'
port = 9192
topic_name = 'rainsty'
group_id = 'rainsty'


def get_topic():
    client = KafkaClient(hosts='{}:{}'.format(host, port))
    print(client.topics)
    topic = client.topics[topic_name]
    print(topic)


def get_message():
    consumer = KafkaConsumer(
        topic_name,
        group_id=group_id,
        auto_offset_reset='earliest',
        bootstrap_servers=['{}:{}'.format(host, port)]
    )
    print('start............................................')
    for message in consumer:
        try:

            message = json.loads(message.value.decode('utf-8'))
            print(message)
            break
        except BaseException as e:
            print('{}: {}'.format(datetime.now(), e))
            continue


def main():
    get_topic()
    get_message()


if __name__ == '__main__':
    main()
