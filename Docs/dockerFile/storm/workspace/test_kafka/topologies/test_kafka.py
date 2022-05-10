"""
Test kafka topology
"""

from streamparse import Grouping, Topology

from spouts.get_kafka import GetKafka
from bolts.put_kafka import PutKafka
from public import config


class TestKafka(Topology):
    
    # get_kafka = GetKafka.spec(config=dict(kafka_config=config.kafka_consumer))
    # put_kafka = PutKafka.spec(inputs=get_kafka, config=dict(kafka_config=config.kafka_producer))

    partitions = config.kafka_consumer.get('partitions').split(',')

    names = locals()
    get_kafka_list = list()
    put_kafka_list = list()

    for p in partitions:
        names['get_kafka_partition_{}'.format(p)] = GetKafka.spec(config=dict(kafka_config=config.kafka_consumer, partition=p))
        get_kafka_list.append(names['get_kafka_partition_{}'.format(p)])

    for i in range(len(partitions)):
        names['put_kafka_partition_{}'.format(partitions[i])] = PutKafka.spec(inputs=get_kafka_list[i],
                                                                              config=dict(kafka_config=config.kafka_producer,
                                                                                          partition=partitions[i]))
        put_kafka_list.append(names['put_kafka_partition_{}'.format(partitions[i])])
