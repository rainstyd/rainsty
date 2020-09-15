# Kafka安装

* 目录结构  

``` text
[root@rainsty kafka]# ll
总用量 8
-rw-r--r-- 1 root root 1312 7月  21 13:52 docker-compose.yml
```

* 文件内容  

    [docker-compose.yml](../dockerFile/kafka/docker-compose.yml)

* 修改kafka外网访问IP  

``` text
vim docker-compose.yml

# 修改每个节点的参数IP
 30     ¦ KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://192.168.0.179:9192
```
  
* 执行安装  

``` text
docker-compose up -d
```

# Kafka命令

* 进入容器  

``` text
docker exec -it kafka01 bash
```

* 查看Topic列表  

``` text
kafka-topics.sh --zookeeper zook01:2181 --list
```

* 创建Topic主题  

``` text
kafka-topics.sh --zookeeper zook01:2181 --create --partitions 24 --replication-factor 1 --topic topicName
```

* 删除Topic主题  

``` text
kafka-topics.sh --zookeeper zook01:2181 --delete --topic topicName
```

* 查看Topic描述  

``` text
kafka-topics.sh --zookeeper zook01:2181 --describe --topic topicName
```

* 生产者Producer生产数据  

``` text
kafka-console-producer.sh --bootstrap-server kafka01:9092,kafka02:9092,kafka03:9092 --topic topicName
```

* 消费者Consumer消费数据  

``` text
kafka-console-consumer.sh --bootstrap-server kafka01:9092,kafka02:9092,kafka03:9092 --topic topicName --group rainsty
```

* 查看Consumer所有消费组  

``` text
kafka-consumer-groups.sh --bootstrap-server kafka01:9092,kafka02:9092,kafka03:9092 --list
```

* 查看Consumer消费组消费情况  

``` text
kafka-consumer-groups.sh --bootstrap-server kafka01:9092,kafka02:9092,kafka03:9092 --describe --group rainsty
```

* 删除Consumer消费组  

``` text
kafka-consumer-groups.sh --bootstrap-server kafka01:9092,kafka02:9092,kafka03:9092 --delete --group rainsty
```

* 修改Topic分区数量  

``` text
# 更改数量应大于现有数量
kafka-topics.sh --zookeeper zook01:2181 --alter --partitions 6 --topic topicName
```

* 修改Topic副本数量

``` text
vim topicName_replication.json

# 新增如下内容  
{
	"version": 1,
	"partitions": [{
			"topic": "topicName",
			"partition": 0,
			"replicas": [1, 2, 3]
		},
		{
			"topic": "topicName",
			"partition": 1,
			"replicas": [1, 2, 3]
		},
		{
			"topic": "topicName",
			"partition": 2,
			"replicas": [1, 2, 3]
		},
		{
			"topic": "topicName",
			"partition": 3,
			"replicas": [1, 2, 3]
		},
		{
			"topic": "topicName",
			"partition": 4,
			"replicas": [1, 2, 3]
		},
		{
			"topic": "topicName",
			"partition": 5,
			"replicas": [1, 2, 3]
		}
	]
}

# 执行修改命令  
kafka-reassign-partitions.sh --zookeeper zook01:2181 --execute --reassignment-json-file topicName_replication.json 

# 没有vim时，如何新建文件并插入内容
bash-4.4# touch a.txt
bash-4.4# cat > a.txt <<EOF
> aaa
> bbb
> ccc
> EOF
bash-4.4# cat a.txt
aaa
bbb
ccc
bash-4.4#
```
