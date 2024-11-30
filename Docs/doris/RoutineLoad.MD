# Doris ROUTINE LOAD

CREATE TABLE rainsty.test_routineload_tbl(
user_id            BIGINT       NOT NULL COMMENT "user id",
name               VARCHAR(20)           COMMENT "name",
age                INT                   COMMENT "age"
)
DUPLICATE KEY(user_id)
DISTRIBUTED BY HASH(user_id) BUCKETS 1;

## csv
CREATE ROUTINE LOAD rainsty.example_routine_load_csv ON test_routineload_tbl
COLUMNS TERMINATED BY ",",
COLUMNS(user_id, name, age)
FROM KAFKA(
"kafka_broker_list" = "192.168.0.188:9094,192.168.0.188:9095,192.168.0.188:9096",
"kafka_topic" = "test-routine-load-csv",
"property.kafka_default_offsets" = "OFFSET_BEGINNING"
);

SHOW ROUTINE LOAD FOR rainsty.example_routine_load_csv;
SHOW ROUTINE LOAD TASK WHERE jobname = 'example_routine_load_csv';

kafka-console-producer.sh --broker-list kafka01:9092,kafka02:9092,kafka03:9092 --topic test-routine-load-csv
1,Emily,25
2,Benjamin,35
3,Olivia,28
4,Alexander,60
5,Ava,17
6,William,69
7,Sophia,32
8,James,64
9,Emma,37
10,Liam,64

PAUSE ROUTINE LOAD FOR rainsty.example_routine_load_csv;
RESUME ROUTINE LOAD FOR rainsty.example_routine_load_csv;
ALTER ROUTINE LOAD FOR rainsty.example_routine_load_csv
PROPERTIES(
"desired_concurrent_number" = "3"
)
FROM KAFKA(
"kafka_broker_list" = "192.168.0.188:9094,192.168.0.188:9095,192.168.0.188:9096",
"kafka_topic" = "test-routine-load-csv-new"
);
STOP ROUTINE LOAD FOR rainsty.example_routine_load_csv;

## json

CREATE ROUTINE LOAD rainsty.example_routine_load_json ON test_routineload_tbl
COLUMNS(user_id,name,age)
PROPERTIES(
"format"="json",
"jsonpaths"="[\"$.user_id\",\"$.name\",\"$.age\"]"
)
FROM KAFKA(
"kafka_broker_list" = "192.168.0.188:9094,192.168.0.188:9095,192.168.0.188:9096",
"kafka_topic" = "test-routine-load-json",
"property.kafka_default_offsets" = "OFFSET_BEGINNING"
);

SHOW ROUTINE LOAD FOR rainsty.example_routine_load_json;
SHOW ROUTINE LOAD TASK WHERE jobname = 'example_routine_load_json';

kafka-console-producer.sh --broker-list kafka01:9092,kafka02:9092,kafka03:9092 --topic test-routine-load-json
{"user_id":1,"name":"Emily","age":25}
{"user_id":2,"name":"Benjamin","age":35}
{"user_id":3,"name":"Olivia","age":28}
{"user_id":4,"name":"Alexander","age":60}
{"user_id":5,"name":"Ava","age":17}
{"user_id":6,"name":"William","age":69}
{"user_id":7,"name":"Sophia","age":32}
{"user_id":8,"name":"James","age":64}
{"user_id":9,"name":"Emma","age":37}
{"user_id":10,"name":"Liam","age":64}

PAUSE ROUTINE LOAD FOR rainsty.example_routine_load_json;
RESUME ROUTINE LOAD FOR rainsty.example_routine_load_json;
ALTER ROUTINE LOAD FOR rainsty.example_routine_load_json
PROPERTIES(
"desired_concurrent_number" = "3"
)
FROM KAFKA(
"kafka_broker_list" = "192.168.0.188:9094,192.168.0.188:9095,192.168.0.188:9096",
"kafka_topic" = "test-routine-load-json-new"
);
STOP ROUTINE LOAD FOR rainsty.example_routine_load_json;
