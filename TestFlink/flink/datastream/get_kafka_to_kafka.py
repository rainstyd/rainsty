import datetime
import json
import logging
import sys
import time
import os

from pyflink.common import Types, SimpleStringSchema, WatermarkStrategy, SerializationSchema
from pyflink.common.serialization import SimpleStringSchema, Encoder
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode, MapFunction, FlatMapFunction, RuntimeContext
from pyflink.datastream.connectors import DeliveryGuarantee
from pyflink.datastream.formats.json import JsonRowSerializationSchema, JsonRowDeserializationSchema
from typing import Any
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import KafkaSource, KafkaSink
from pyflink.datastream.connectors.kafka import KafkaOffsetsInitializer, KafkaOffsetResetStrategy, KafkaRecordSerializationSchema

# 解决os输出中文乱码问题
os.environ['JAVA_TOOL_OPTIONS'] = '-Dfile.encoding=UTF-8'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")


class StringToListJsonMap(MapFunction):
    def map(self, value):
        result = []
        value = value.split('----------')
        for v in value:
            _dict = {}
            v = v.split('\n')

            _dict['logType'.lower()] = v[0][:2]
            _dict['uniqueStr'.lower()] = v[0].split(">")[1].split("[")[0]

            for d in v[1:]:
                d = d.split('=', 1)
                if len(d) == 2:
                    _dict[d[0].lower()] = d[1]

            result.append(_dict)
        result = json.dumps(result, ensure_ascii=False)
        print(datetime.datetime.now().__str__())
        return result


class ToTransData(object):
    def __init__(self):
        pass

    @staticmethod
    def to_lower(_str: str):
        return _str.lower()


class StringToDictJsonFlatMap(FlatMapFunction):

    def __init__(self, split_sep='----------'):
        self.to_trans_data = None
        self.split_sep = split_sep

    def open(self, runtime_context: RuntimeContext):
        self.to_trans_data = ToTransData()

    def flat_map(self, value):
        value = value.split(self.split_sep)
        for v in value:
            _dict = {}
            v = v.split('\n')

            _dict[self.to_trans_data.to_lower('logType')] = v[0][:2]
            _dict[self.to_trans_data.to_lower('uniqueStr')] = v[0].split(">")[1].split("[")[0]

            for d in v[1:]:
                d = d.split('=', 1)
                if len(d) == 2:
                    _dict[d[0].lower()] = d[1]

            print(datetime.datetime.now().__str__())
            yield json.dumps(_dict)


if __name__ == '__main__':
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_runtime_mode(RuntimeExecutionMode.STREAMING)

    env.set_parallelism(1)
    bootstrap_servers = '192.168.0.188:9094,192.168.0.188:9095,192.168.0.188:9096'
    topic_name_src = 'flink_kafka'
    topic_name_des = 'flink_kafka2'

    # 本地运行需要设置依赖的jar包，提交flink集群要注释掉env.add_jars
    # env.add_jars("/root/deploy/flink-1.17.1/lib/flink-connector-kafka-1.17.1.jar")
    # env.add_jars("file:\\D:\\Downloads\\ChormeDownloads\\flink-sql-connector-kafka-1.17.1.jar")

    print("start get_kafka_to_kafka")

    source = KafkaSource.builder() \
        .set_bootstrap_servers(bootstrap_servers) \
        .set_topics(topic_name_src) \
        .set_value_only_deserializer(SimpleStringSchema()) \
        .set_starting_offsets(KafkaOffsetsInitializer.latest()) \
        .build()

    source_stream = env.from_source(
        source=source,
        watermark_strategy=WatermarkStrategy.no_watermarks(),
        source_name="kafkaSource")

    data_stream = source_stream.map(StringToListJsonMap(), output_type=Types.STRING())
    # data_stream = source_stream.flat_map(StringToDictJsonFlatMap(), output_type=Types.STRING())
    data_stream.print()

    serializer = KafkaRecordSerializationSchema.builder() \
        .set_topic(topic_name_des) \
        .set_key_serialization_schema(SimpleStringSchema()) \
        .set_value_serialization_schema(SimpleStringSchema()) \
        .build()

    sink = KafkaSink.builder() \
        .set_bootstrap_servers(bootstrap_servers) \
        .set_record_serializer(serializer) \
        .build()

    data_stream.sink_to(sink)

    env.execute('flink.datastream.get_kafka_to_kafka')
