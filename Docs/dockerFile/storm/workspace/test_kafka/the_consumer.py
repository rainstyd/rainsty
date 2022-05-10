# -*- encoding: utf-8 -*-

from confluent_kafka import Consumer
from confluent_kafka import TopicPartition


# latest earliest none
topic_name = 'b'
group_id = 'b1'
bootstrap_servers = '127.0.0.1:8704,127.0.0.1:8704,127.0.0.1:8704'

consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'default.topic.config': {
        'enable.auto.commit': True,
        'auto.offset.reset': 'latest',
        'auto.commit.interval.ms': 1000,
        'fetch.wait.max.ms': 1000
    }
})

# consumer.assign([TopicPartition(topic=topic_name, partition=0)])
consumer.subscribe(topics=[topic_name])


while True:
    msg = consumer.poll(1)

    if msg is None:
        print('......')
        continue
    else:
        # data = eval(msg.value().decode())
        # if data['stockcode'] == '002943':
        #     print(data)
        #     break
        print(msg.value())
        # print('11111111')
        # consumer.commit()
        # else:
        #     print('-')
        #     continue
