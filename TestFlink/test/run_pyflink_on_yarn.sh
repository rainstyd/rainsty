
#打造虚拟环境包
bin/python3.10 -m pip install virtualenv  -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
bin/virtualenv --python=3.10.14 --never-download test_flink_1171_env_py31014
test_flink_1171_env_py31014/bin/python -m pip install -r test_flink_1171_env_py31014.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
zip -r test_flink_1171_env_py31014.zip test_flink_1171_env_py31014

#打包上传至hdfs
cd /data/deploy/hadoop-3.3.6
bin/hdfs dfs -mkdir -p /user/rainsty
bin/hdfs dfs -put /data/deploy/Python-3.10.14/test_flink_1171_env_py31014.zip /user/rainsty/

#flink目录
cd /data/deploy/flink-1.17.1

#本地测试运行
/data/deploy/Python-3.10.14/bin/python3.10 rainsty/flink/datastream/get_kafka_to_kafka.py

#本地提交运行
bin/flink run -pyexec /data/deploy/Python-3.10.14/bin/python3.10 -py rainsty/flink/datastream/get_kafka_to_kafka.py

#Yarn提交运行
/data/deploy/flink-1.17.1/bin/flink run-application -t yarn-application \
-Dyarn.application.name=get_kafka_to_kafka \
-Dtaskmanager.memory.process.size=1024M \
-Dtaskmanager.numberOfTaskSlots=1 \
-Dparallelism.default=1 \
-Dyarn.ship-files=/data/deploy/flink-1.17.1/rainsty \
-pyarch hdfs://develop:9000/user/rainsty/test_flink_1171_env_py31014.zip \
-pyexec test_flink_1171_env_py31014.zip/test_flink_1171_env_py31014/bin/python3.10 \
-pyclientexec test_flink_1171_env_py31014.zip/test_flink_1171_env_py31014/bin/python3.10 \
-pyfs rainsty \
-pym flink.datastream.get_kafka_to_kafka
