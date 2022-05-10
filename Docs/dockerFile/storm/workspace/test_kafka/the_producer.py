# -*- encoding: utf-8 -*-

import confluent_kafka
import time
import datetime


bootstrap_servers = '127.0.0.1:8704,127.0.0.1:8704,127.0.0.1:8704'


topic_name = 'a'


producer = confluent_kafka.Producer({'bootstrap.servers': bootstrap_servers})


msg_index = 1
while True:
    msg = datetime.datetime.now().__str__() + ' ' + str(msg_index)
    # producer.produce(topic=topic_name, value=msg.encode(), partition=0)
    producer.produce(topic=topic_name, value=msg.encode())
    producer.flush()
    print(msg)
    msg_index += 1
    time.sleep(1)
