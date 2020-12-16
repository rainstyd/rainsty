# Mysql安装  

* 目录结构  

``` text
root@rainsty:mysql# ll
total 8
-rw-r--r-- 1 root root  448 Aug 17 17:09 docker-compose.yml
drwxr-xr-x 4 root root 4096 Aug 17 17:41 volumes/
root@rainsty:mysql# ll volumes/
total 8
drwxr-xr-x 6  999 root 4096 Aug 17 17:41 data/
drwxr-xr-x 2 root root 4096 Aug 17 17:06 mysql.conf.d/
root@rainsty:mysql# ll volumes/mysql.conf.d/
total 4
-rw-r--r-- 1 root root 1938 Aug 17 17:06 my.cnf
```

* 文件内容  

    [docker-compose.yml](../dockerFile/mysql/docker-compose.yml)
    [my.cnf](../dockerFile/mysql/volumes/mysql.conf.d/my.cnf)
    
* 执行安装  

``` text
docker-compose up -d
```

# Mysql命令  

* 进入容器  

``` text
docker exec -it mysql bash
```

* 进入Mysql终端  

``` text
mysql -uroot -p123456
```

* 创建用户  

``` text
CREATE USER 'rainsty'@'%' IDENTIFIED BY '123456';
```

* 赋予Navicat登陆权限  

``` text
ALTER USER rainsty IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY '123456';
```

* 赋予远程登陆权限  

``` text
GRANT ALL PRIVILEGES ON *.* TO rainsty@'%';
```

* 刷新权限  

``` text
FLUSH PRIVILEGES;
```

# Mysql常用语法  

## Mysql基础语句  

### 创建DATABASE  

``` text
CREATE DATABASE rainsty;
```

### 切换DATABASE  

``` text
USE rainsty;
```

### 创建TABLE  

``` text
CREATE TABLE `student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `student_id` int(10) NOT NULL COMMENT '学生编号',
  `name` varchar(16) NOT NULL COMMENT '学生姓名',
  `sex` int(1) DEFAULT NULL COMMENT '性别: 1-男, 2-女;',
  `input_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `update_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_student_id` (`student_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='学生表';
```  

### INSERT数据  

``` text
INSERT INTO student (student_id, name, sex) values (2020050101, '郭尽一', 1);
INSERT INTO student (student_id, name, sex) values (2020050102, '郭尽二', 2);
INSERT INTO student (student_id, name, sex) values (2020050103, '郭尽三', 1);
INSERT INTO student (student_id, name, sex) values (2020050104, '郭尽四', 1);
INSERT INTO student (student_id, name, sex) values (2020050105, '郭尽五', 2);
INSERT INTO student (student_id, name, sex) values (2020050106, '郭尽六', 1);
INSERT INTO student (student_id, name, sex) values (2020050107, '郭尽七', 2);
INSERT INTO student (student_id, name, sex) values (2020050108, '郭尽八', 2);
INSERT INTO student (student_id, name, sex) values (2020050109, '郭尽九', 1);
INSERT INTO student (student_id, name, sex) values (2020050110, '郭尽十', 1);
```

### UPDATE数据  

``` text
UPDATE student SET name='郭吾十',sex=2 WHERE student_id=2020050110;
```

### DELETE数据  

``` text
DELETE FROM student WHERE student_id=2020050110;
```

### ALTER表  

``` text
# 修改表名称
ALTER TABLE `rainsty`.`student` RENAME TO `rainsty`.`student01`;
ALTER TABLE `rainsty`.`student01` RENAME TO `rainsty`.`student`;
# 修改表字段类型
ALTER TABLE `rainsty`.`student` CHANGE COLUMN `student_id` `studentid` INT(20) NOT NULL COMMENT '学生编号1'
ALTER TABLE `rainsty`.`student` CHANGE COLUMN `studentid` `student_id` INT(10) NOT NULL COMMENT '学生编号'
# 增加表字段
ALTER TABLE `rainsty`.`student` ADD COLUMN `age` INT(3) DEFAULT NULL COMMENT '学生年龄' AFTER `sex`;
# 删除字段
ALTER TABLE `rainsty`.`student` DROP COLUMN `age`;
```

### DROP表  

``` text
删除表
DROP TABLE `rainsty`.`student`;
```

### 创建FUNCTION  

``` text
DELIMITER ;;
CREATE DEFINER=`root`@`%` FUNCTION `rainsty`(`aaa` int(2),`bbb` int(2)) RETURNS decimal(20,6)
BEGIN

	DECLARE c DECIMAL(20,6);
	
	SELECT (aaa+bbb) C INTO c;

RETURN c;
END
;;
DELIMITER ;
```

``` text
# 调用函数
select rainsty(111,222);
```

## Mysql查询  

``` text
# 创建表基础数据
CREATE TABLE `student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `student_id` int(10) NOT NULL COMMENT '学生编号',
  `name` varchar(16) NOT NULL COMMENT '学生姓名',
  `sex` int(1) DEFAULT NULL COMMENT '性别: 1-男, 2-女;',
  `input_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `update_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_student_id` (`student_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='学生表';

INSERT INTO student (student_id, name, sex) values (2020050101, '郭尽一', 1);
INSERT INTO student (student_id, name, sex) values (2020050102, '郭尽二', 2);
INSERT INTO student (student_id, name, sex) values (2020050103, '郭尽三', 1);
INSERT INTO student (student_id, name, sex) values (2020050104, '郭尽四', 1);
INSERT INTO student (student_id, name, sex) values (2020050105, '郭尽五', 2);
INSERT INTO student (student_id, name, sex) values (2020050106, '郭尽六', 1);
INSERT INTO student (student_id, name, sex) values (2020050107, '郭尽七', 2);
INSERT INTO student (student_id, name, sex) values (2020050108, '郭尽八', 2);
INSERT INTO student (student_id, name, sex) values (2020050109, '郭尽九', 1);
INSERT INTO student (student_id, name, sex) values (2020050110, '郭尽十', 1);

CREATE TABLE `academic` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `student_id` int(10) NOT NULL COMMENT '学生编号',
  `year` int(10) NOT NULL COMMENT '学年',
  `term` int(1) NOT NULL COMMENT '学期: 1:上学期, 2:下学期',
  `english` int(3) DEFAULT NULL COMMENT '英语成绩',
  `math` int(3) DEFAULT NULL COMMENT '数学成绩',
  `input_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `update_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_student_id` (`student_id`, `year`, `term`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='成绩表';

INSERT INTO academic (student_id, year, term, english, math) values (2020050101, 2020, 1, 80, 92);
INSERT INTO academic (student_id, year, term, english, math) values (2020050101, 2020, 2, 83, 71);
INSERT INTO academic (student_id, year, term, english, math) values (2020050102, 2020, 1, 70, 82);
INSERT INTO academic (student_id, year, term, english, math) values (2020050102, 2020, 2, 81, 81);
INSERT INTO academic (student_id, year, term, english, math) values (2020050103, 2020, 1, 53, 72);
INSERT INTO academic (student_id, year, term, english, math) values (2020050103, 2020, 2, 63, 69);
INSERT INTO academic (student_id, year, term, english, math) values (2020050104, 2020, 1, 90, 82);
INSERT INTO academic (student_id, year, term, english, math) values (2020050104, 2020, 2, 30, 76);
INSERT INTO academic (student_id, year, term, english, math) values (2020050105, 2020, 1, 87, 75);
INSERT INTO academic (student_id, year, term, english, math) values (2020050105, 2020, 2, 89, 81);
INSERT INTO academic (student_id, year, term, english, math) values (2020050106, 2020, 1, 70, 91);
INSERT INTO academic (student_id, year, term, english, math) values (2020050106, 2020, 2, 63, 01);
INSERT INTO academic (student_id, year, term, english, math) values (2020050107, 2020, 1, 48, 98);
INSERT INTO academic (student_id, year, term, english, math) values (2020050107, 2020, 2, 73, 84);
INSERT INTO academic (student_id, year, term, english, math) values (2020050108, 2020, 1, 64, 68);
INSERT INTO academic (student_id, year, term, english, math) values (2020050108, 2020, 2, 78, 51);
INSERT INTO academic (student_id, year, term, english, math) values (2020050109, 2020, 1, 86, 79);
INSERT INTO academic (student_id, year, term, english, math) values (2020050109, 2020, 2, 87, 68);
INSERT INTO academic (student_id, year, term, english, math) values (2020050110, 2020, 1, 94, 72);
INSERT INTO academic (student_id, year, term, english, math) values (2020050110, 2020, 2, 99, 81);

```  

### 基础查询

#### WHERE(过滤条件)
``` text
SELECT 
    *
FROM
    `student`
WHERE
    student_id > 2020050106;
```

#### ORDER(排序)
``` text
# 单字段排序
SELECT 
    *
FROM
    `student`
ORDER BY student_id DESC;
# 多字段排序
SELECT 
    *
FROM
    `student`
ORDER BY student_id DESC, name ASC;
```

#### LIMIT(取多少条)
``` text
SELECT 
    *
FROM
    `student`
LIMIT 10
```

#### OFFSET(从第几条开始取多少条)
``` text
SELECT 
    *
FROM
    `student`
LIMIT 10 OFFSET 0
```

#### AS(字段设置别名和表设置别名, 可省略AS)
``` text
SELECT 
    a.student_id AS sid
FROM
    `student` a
```

#### AS临时表(用双括号包起来的查询语句)
``` text
SELECT 
    *
FROM
    (SELECT 
        *
    FROM
        `student`) a
WHERE
    a.sex = 1
```

#### LIKE(模糊查询,%为通配符)

``` text
SELECT 
    *
FROM
    `student`
WHERE
    name LIKE '%一' OR name LIKE '郭%'
        OR name LIKE '%尽%'
```

#### IN(表示字段值在一个集合里)
``` text
SELECT 
    *
FROM
    `student`
WHERE
    student_id IN (2020050103 , 2020050107)
```

#### NOT IN(表示字段值不在一个集合里)
``` text
SELECT 
    *
FROM
    `student`
WHERE
    student_id NOT IN (2020050103 , 2020050107)
```

#### IS NULL(表示字段值为NULL)
``` text
SELECT 
    *
FROM
    `student`
WHERE
    student_id IS NULL
```

#### IS NOT NULL(表示字段值为不NULL)
``` text
SELECT 
    *
FROM
    `student`
WHERE
    student_id IS NOT NULL
```

#### WHERE多条件AND
``` text
SELECT 
    a.id, a.name, a.*
FROM
    `student` a
WHERE
    student_id > 2020050106 AND a.sex = 2;
    
```

#### WHERE多条件OR
``` text
SELECT 
    a.id, a.name, a.*
FROM
    `student` a
WHERE
    student_id = 2020050106
        OR student_id = 2020050107;

```

#### WHERE多条件AND和OR共用
``` text
SELECT 
    a.id, a.name, a.*
FROM
    `student` a
WHERE
    (student_id = 2020050106
        OR student_id = 2020050107)
        AND a.sex = 2;
```

### 高级查询  

#### WHERE多表查询  

``` text
SELECT 
    *
FROM
    `student` a,
    `academic` b
WHERE
    a.student_id = b.student_id
```

#### 左连接  

``` text
SELECT 
    *
FROM
    `student` a
        LEFT JOIN
    `academic` b ON a.student_id = b.student_id
```

#### 右连接  

``` text
SELECT 
    *
FROM
    `student` a
        RIGHT JOIN
    `academic` b ON a.student_id = b.student_id
```

#### 内连接  

``` text
SELECT 
    *
FROM
    `student` a
        INNER JOIN
    `academic` b ON a.student_id = b.student_id
```

#### 右外连接  

``` text
SELECT 
    *
FROM
    `student` a
        RIGHT OUTER JOIN
    `academic` b ON a.student_id = b.student_id
```

#### GROUP(分组，求数量，求总和，求平均，数据去重)

``` text
# 分组求数量（求男生和女生的数量）
SELECT 
    sex, COUNT(sex)
FROM
    `student`
GROUP BY sex

# 分组求总和（求2020各学期英语总成绩）
SELECT 
    term, SUM(english)
FROM
    `academic`
WHERE
    year = 2020
GROUP BY term

# 分组求总和（求2020各学期英语平均成绩）
SELECT 
    term, AVG(english)
FROM
    `academic`
WHERE
    year = 2020
GROUP BY term

# 分组数据去重（求2020各学期英语最高成绩）
SELECT 
    *
FROM
    (SELECT 
        term, english
    FROM
        `academic`
    WHERE
        year = 2020
    GROUP BY term , english
    ORDER BY term , english DESC) a
GROUP BY term
```

## Mysql字符串函数  

### ASCII(s)   

``` text
# 返回字符串 s 的第一个字符的 ASCII 码。	
select ASCII("Sky love Ocean!")
```

### CHAR_LENGTH(s)   

``` text
# 返回字符串 s 的字符数
select CHAR_LENGTH("Sky love Ocean!")
```

### CHARACTER_LENGTH(s)   

``` text
# 返回字符串 s 的字符数
select CHARACTER_LENGTH("Sky love Ocean!")
```

### CONCAT(s1,s2...sn)   

``` text
# 字符串 s1,s2 等多个字符串合并为一个字符串
select CONCAT("Sky ", "love ", "Ocean!")
```

### CONCAT_WS(x, s1,s2...sn)   

``` text
# 同 CONCAT(s1,s2,...) 函数，但是每个字符串之间要加上 x，x 可以是分隔符
select CONCAT_WS(" ", "Sky", "love", "Ocean!")
```
	
### FIELD(s,s1,s2...)   

``` text
# 返回第一个字符串 s 在字符串列表(s1,s2...)中的位置
select FIELD("love", "Sky", "love", "Ocean!")
```

### FIND_IN_SET(s1,s2)   

``` text
# 返回在字符串s2中与s1匹配的字符串的位置
select FIND_IN_SET("love", "Sky,love,Ocean!")
```

### INSERT(s1,x,len,s2)   

``` text
# 字符串 s2 替换 s1 的 x 位置开始长度为 len 的字符串	
select INSERT("Sky love Ocean!", 5, 1, "L")
```

### LOCATE(s1,s)	   

``` text
# 从字符串 s 中获取 s1 的开始位置		
select LOCATE("love", "Sky love Ocean!")
```

### LCASE(s)		   

``` text
# 将字符串 s 的所有字母变成小写字母			
select LCASE("Sky love Ocean!")
```

### LEFT(s,n)		   

``` text
# 返回字符串 s 的前 n 个字符			
select LEFT("Sky love Ocean!", 5)
```

### LOWER(s)		   

``` text
# 将字符串 s 的所有字母变成小写字母		
select LOWER("Sky love Ocean!")
```

### LPAD(s1,len,s2)		   

``` text
# 在字符串 s1 的开始处填充字符串 s2，使字符串长度达到 len			
select LPAD("love", 50, "Sky love Ocean!")
```

### LTRIM(s)		   

``` text
# 去掉字符串 s 开始处的空格			
select LTRIM("   Sky love Ocean!")
```

### MID(s,n,len)		   

``` text
# 从字符串 s 的 n 位置截取长度为 len 的子字符串，同 SUBSTRING(s,n,len)			
select MID("Sky love Ocean!", 5, 4)
```

### POSITION(s1 IN s)		   

``` text
# 从字符串 s 中获取 s1 的开始位置			
select POSITION("love" IN "Sky love Ocean!")
```

### REPEAT(s,n)		   

``` text
# 将字符串 s 重复 n 次			
select REPEAT("love", 10)
```

### REPLACE(s,s1,s2)		   

``` text
# 将字符串 s2 替代字符串 s 中的字符串 s1			
select REPLACE("Sky love Ocean!", "love", "Love")
```

### REVERSE(s)		   

``` text
# 将字符串s的顺序反过来			
select REVERSE("Sky love Ocean!")
```

### RIGHT(s,n)		   

``` text
# 从字符串 s 中获取 s1 的开始位置		
select RIGHT("Sky love Ocean!", 6)
```

### RPAD(s1,len,s2)		   

``` text
# 在字符串 s1 的结尾处添加字符串 s2，使字符串的长度达到 len			
select RPAD("Sky love Ocean!", 50, "Love")
```

### RTRIM(s)		   

``` text
# 去掉字符串 s 结尾处的空格			
select RTRIM("Sky love Ocean!   ")
```

### SPACE(n)		   

``` text
# 返回 n 个空格			
select SPACE(10)
```

### STRCMP(s1,s2)		   

``` text
# 比较字符串 s1 和 s2，如果 s1 与 s2 相等返回 0 ，如果 s1>s2 返回 1，如果 s1<s2 返回 -1			
select STRCMP("love", "Sky love Ocean!")
```

### SUBSTR(s, start, length)		   

``` text
# 从字符串 s 的 start 位置截取长度为 length 的子字符串			
select SUBSTR("Sky love Ocean!", 5, 10)
```

### SUBSTRING(s, start, length)		   

``` text
# 从字符串 s 的 start 位置截取长度为 length 的子字符串			
select SUBSTRING("Sky love Ocean!", 5, 10)
```

### SUBSTRING_INDEX(s, delimiter, number)		   

``` text
# 返回从字符串 s 的第 number 个出现的分隔符 delimiter 之后的子串。
# 如果 number 是正数，返回第 number 个字符左边的字符串。
# 如果 number 是负数，返回第(number 的绝对值(从右边数))个字符右边的字符串。			
select SUBSTRING_INDEX("Sky love Ocean!", " ", 1)
select SUBSTRING_INDEX("Sky love Ocean!", " ", -1)
```

### TRIM(s)		   

``` text
# 去掉字符串 s 开始和结尾处的空格			
select TRIM("   Sky love Ocean!    ")
```

### UCASE(s)		   

``` text
# 将字符串转换为大写			
select UCASE("Sky love Ocean!")
```

### UPPER(s)		   

``` text
# 将字符串转换为大写		
select UPPER("Sky love Ocean!")
```

## Mysql数字函数  

### ABS(x)  

``` text
# 返回 x 的绝对值　　	
select ABS(-5.201314)
```

### ACOS  

``` text	
# 求 x 的反余弦值(参数是弧度)		
select ACOS(0.25)
```

### ASIN(x)	  

``` text
# 求反正弦值(参数是弧度)			
select ASIN(0.25)
```

### ATAN(x)	  

``` text
# 求反正切值(参数是弧度)	  		
select ATAN(0.25)
```

### ATAN2(n, m)	  

``` text
# 求反正切值(参数是弧度)	  		
select ATAN2(-0.8, 2)
```

### AVG(expression)	  

``` text
# 返回一个表达式的平均值，expression 是一个字段	  		
select AVG(price) from (select 0.5 price union select 0.7 price)
```

### CEIL(x)	  

``` text
# 返回大于或等于 x 的最小整数　	  		
select CEIL(5.201314)
```

### CEILING(x)	  

``` text
# 返回大于或等于 x 的最小整数　  		
select CEILING(5.201314)
```

### COS(x)	  

``` text
# 求余弦值(参数是弧度)	  		
select COS(5.2)
```

### COT(x)	  

``` text
# 求余切值(参数是弧度)	  		
select COT(5.2)
```

### COUNT(expression)	  

``` text
# 返回查询的记录总数，expression 参数是一个字段或者 * 号	  		
select COUNT(c) from (select 5 c union select 6 c union select 7 c) a
```

### DEGREES(x)	  

``` text
# 将弧度转换为角度　　	  		
select DEGREES(5.2)
```

### n DIV m	  

``` text
# 整除，n 为被除数，m 为除数	  		
select 10 DIV 2
```

### EXP(x)	  

``` text
# 返回 e 的 x 次方　　	  		
select EXP()
```

### FLOOR(x)	  

``` text
# 返回小于或等于 x 的最大整数　　	  		
select FLOOR(5.2)
```

### FORMAT(x,n)  

``` text
# 函数可以将数字 x 进行格式化 "#,###.##", 将 x 保留到小数点后 n 位，最后一位四舍五入。
select FORMAT(52.131400, 4)
```

### GREATEST(expr1, expr2, expr3, ...)	  

``` text
# 返回列表中的最大值	(隐士转换类型)  		
select GREATEST(1, 4, 5.2, 9)
```

### LEAST(expr1, expr2, expr3, ...)	  

``` text
# 返回列表中的最小值	  		
select LEAST(1, 4, 5.2, 9)
```

### LN(x)  

``` text
# 返回数字x的自然对数，以 e 为底。	  		
select LN(2)
```

### LOG(x) 或 LOG(base, x)	  

``` text
# 返回自然对数(以 e 为底的对数)，如果带有 base 参数，则 base 为指定带底数。　　	  		
select LOG(2) union select LOG(2, 3)
```

### LOG10(x)	  

``` text
# 返回以 10 为底的对数　　	  		
select LOG10(2)
```

### LOG2(x)	  

``` text
# 返回以 2 为底的对数　　  		
select LOG2(2)
```

### MAX(expression)	  

``` text
# 返回字段 expression 中的最大值	  		
select MAX(c) from (select 5 c union select 2 c) a
```

### MIN(expression)	  

``` text
# 返回字段 expression 中的最小值	  		
select MIN(c) from (select 5 c union select 2 c) a
```

### MOD(x,y)	  

``` text
# 返回 x 除以 y 以后的余数　	  		
select MOD(5, 2)
```

### PI()	  

``` text
# 返回圆周率(3.141593）　　	  		
select PI()
```

### POW(x,y)	  

``` text
# 返回 x 的 y 次方　	  		
select POW(2, 3)
```

### POWER(x, y)   

``` text
# 返回 x 的 y 次方　	  		
select POWER(2, 3)
```

### RADIANS(x)	  

``` text
# 将角度转换为弧度　　	  		
select RADIANS(180)
```

### RAND()	  

``` text
# 返回 0 到 1 的随机数　　	  		
select RAND()
```

### ROUND(x, n)	  

``` text
# 返回离 x 最近的整数	,n 为小数点后位数，默认为0， 四舍五入  		
select ROUND(5.2013149) union select ROUND(5.2013149, 6)
```

### SIGN(x)	  

``` text
# 返回 x 的符号，x 是负数、0、正数分别返回 -1、0 和 1　	  		
select SIGN(5)
```

### SIN(x)	  

``` text
# 求正弦值(参数是弧度)　　	  		
select SIN(31)
```

### SQRT(x)	  

``` text
# 返回x的平方根　　	  		
select SQRT(2)
```

### SUM(expression)	  

``` text
# 返回指定字段的总和	  		
select SUM(c) from (select 5 c union select 6 c) a
```

### TAN(x)	  

``` text
# 求正切值(参数是弧度)	  		
select TAN(5.2)
```

### TRUNCATE(x,y)	  

``` text
# 返回数值 x 保留到小数点后 y 位的值（与 ROUND 最大的区别是不会进行四舍五入）	  		
select TRUNCATE(5.201314, 3)
```

## MySQL日期函数  

### ADDDATE(d,n)	  

``` text
# 计算起始日期 d 加上 n 天的日期	  		
SELECT ADDDATE("2017-06-15", INTERVAL 10 DAY)
```

### ADDTIME(t,n)	  

``` text
# n 是一个时间表达式，时间 t 加上时间表达式 n	  		
SELECT ADDTIME('2011-11-11 11:11:11', 5)
```

### CURDATE()	  

``` text
# 返回当前日期	  		
select CURDATE()
```

### CURRENT_DATE()	  

``` text
# 返回当前日期	  		
select CURRENT_DATE()
```

### CURRENT_TIME	  

``` text
# 返回当前时间	  		
select CURRENT_TIME()
```

### CURRENT_TIMESTAMP()	  

``` text
# 返回当前日期和时间	  		
select CURRENT_TIMESTAMP(6)
```

### CURTIME()	  

``` text
# 返回当前时间	  		
select CURTIME()
```

### DATE()	  

``` text
# 从日期或日期时间表达式中提取日期值	
SELECT DATE("2017-06-15")
```

### DATEDIFF(d1,d2)	  

``` text
# 计算日期 d1->d2 之间相隔的天数	  		
SELECT DATEDIFF('2001-01-01','2001-02-02')
```

### DATE_ADD(d，INTERVAL expr type)	  

``` text
# 计算起始日期 d 加上一个时间段后的日期(默认是天)	  		
SELECT ADDDATE('2011-11-11 11:11:11',1) union SELECT ADDDATE('2011-11-11 11:11:11', INTERVAL 5 MINUTE)
```

### DATE_FORMAT(d,f)	  

``` text
# 按表达式 f的要求显示日期 d	  		
SELECT DATE_FORMAT('2011-11-11 11:11:11','%Y-%m-%d %H:%i:%S')
```

### DATE_SUB(date,INTERVAL expr type)	  

``` text
# 函数从日期减去指定的时间间隔。	  		
select DATE_SUB('2011-11-11 11:11:11', INTERVAL 2 day)
```

### DAY(d)	  

``` text
# 返回日期值 d 的日期部分	  		
select DAY('2011-11-11 11:11:11')
```

### DAYNAME(d)	  

``` text
# 返回日期 d 是星期几，如 Monday,Tuesday	  		
select DAYNAME('2011-11-11 11:11:11')
```

### DAYOFMONTH(d)	  

``` text
# 计算日期 d 是本月的第几天	  		
select DAY('2011-11-11 11:11:11')
```

### DAYOFWEEK(d)	  

``` text
# 日期 d 今天是星期几，1 星期日，2 星期一，以此类推	  		
select DAYOFWEEK('2011-11-11 11:11:11')
```

### DAYOFYEAR(d)	  

``` text
# 计算日期 d 是本年的第几天	  		
select DAYOFYEAR('2011-11-11 11:11:11')
```

### EXTRACT(type FROM d)

``` text
# AAAA  		
select DAY('2011-11-11 11:11:11')
```

### AAA  

``` text
# 从日期 d 中获取指定的值，type 指定返回的值。
type可取值为：
MICROSECOND
SECOND
MINUTE
HOUR
DAY
WEEK
MONTH
QUARTER
YEAR
SECOND_MICROSECOND
MINUTE_MICROSECOND
MINUTE_SECOND
HOUR_MICROSECOND
HOUR_SECOND
HOUR_MINUTE
DAY_MICROSECOND
DAY_SECOND
DAY_MINUTE
DAY_HOUR
YEAR_MONTH

SELECT EXTRACT(MINUTE FROM '2011-11-11 11:11:11')
```

### FROM_DAYS(n)

``` text
# 计算从 0000 年 1 月 1 日开始 n 天后的日期
SELECT FROM_DAYS(1111)
```

### HOUR(t)

``` text
# 返回 t 中的小时值
select HOUR('2011-11-11 11:11:11')
```

### LAST_DAY(d)

``` text
# 返回给给定日期的那一月份的最后一天
select LAST_DAY('2011-11-11 11:11:11')
```

### LOCALTIME()

``` text
# 返回当前日期和时间
select LOCALTIME()
```

### LOCALTIMESTAMP()

``` text
# 返回当前日期和时间
select LOCALTIMESTAMP()
```

### MAKEDATE(year, day-of-year)

``` text
# 基于给定参数年份 year 和所在年中的天数序号 day-of-year 返回一个日期
select MAKEDATE(2019, 100)
```

### MAKETIME(hour, minute, second)

``` text
# 组合时间，参数分别为小时、分钟、秒
SELECT MAKETIME(11, 35, 4);
```

### MICROSECOND(date)

``` text
# 返回日期参数所对应的微秒数
SELECT MICROSECOND("2017-06-20 09:34:00.000023");
```

### MINUTE(t)

``` text
# 返回 t 中的分钟值
SELECT MINUTE('1:2:3')
```

### MONTHNAME(d)

``` text
# 返回日期当中的月份名称，如 November
SELECT MONTHNAME('2011-11-11 11:11:11')
```

### MONTH(d)

``` text
# 返回日期d中的月份值，1 到 12
SELECT MONTH('2011-11-11 11:11:11')
```

### NOW()

``` text
# 返回当前日期和时间
select NOW()
```

### PERIOD_ADD(period, number)

``` text
# 为 年-月 组合日期添加一个时段
SELECT PERIOD_ADD(201703, 5);
```

### PERIOD_DIFF(period1, period2)

``` text
# 返回两个时段之间的月份差值
SELECT PERIOD_DIFF(201710, 201703);
```

### QUARTER(d)

``` text
# 返回日期d是第几季节，返回 1 到 4
SELECT QUARTER('2011-11-11 11:11:11')
```

### SECOND(t)

``` text
# 返回 t 中的秒钟值
SELECT SECOND('1:2:3')
```

### SEC_TO_TIME(s)

``` text
# 将以秒为单位的时间 s 转换为时分秒的格式
SELECT SEC_TO_TIME(4320)
```

### STR_TO_DATE(string, format_mask)

``` text
# 将字符串转变为日期
SELECT STR_TO_DATE("August 10 2017", "%M %d %Y");
```

### SUBDATE(d,n)

``` text
# 日期 d 减去 n 天后的日期
SELECT SUBDATE('2011-11-11 11:11:11', 1)
```

### SUBTIME(t,n)

``` text
# 时间 t 减去 n 秒的时间
SELECT SUBTIME('2011-11-11 11:11:11', 5)
```

### SYSDATE()

``` text
# 返回当前日期和时间
SELECT SYSDATE()
```

### TIME(expression)

``` text
# 提取传入表达式的时间部分
SELECT TIME("19:30:10");
```

### TIME_FORMAT(t,f)

``` text
# 按表达式 f 的要求显示时间 t
SELECT TIME_FORMAT('11:11:11','%r')
```

### TIME_TO_SEC(t)

``` text
# 将时间 t 转换为秒
SELECT TIME_TO_SEC('1:12:00')
```

### TIMEDIFF(time1, time2)

``` text
# 计算时间差值
SELECT TIMEDIFF("13:10:11", "13:10:10");
```

### TIMESTAMP(expression, interval)

``` text
# 单个参数时，函数返回日期或日期时间表达式；有2个参数时，将参数加和
SELECT TIMESTAMP("2017-07-23",  "13:10:11");
```

### TO_DAYS(d)

``` text
# 计算日期 d 距离 0000 年 1 月 1 日的天数
SELECT TO_DAYS('0001-01-01 01:01:01')
```

### WEEK(d)

``` text
# 计算日期 d 是本年的第几个星期，范围是 0 到 53
SELECT WEEK('2011-11-11 11:11:11')
```

### WEEKDAY(d)

``` text
# 日期 d 是星期几，0 表示星期一，1 表示星期二
SELECT WEEKDAY("2017-06-15");
```

### WEEKOFYEAR(d)

``` text
# 计算日期 d 是本年的第几个星期，范围是 0 到 53
SELECT WEEKOFYEAR('2011-11-11 11:11:11')
```

### YEAR(d)

``` text
# 返回年份
SELECT YEAR("2017-06-15");
```

### YEARWEEK(date, mode)

``` text
# 返回年份及第几周（0到53），mode 中 0 表示周天，1表示周一，以此类推
SELECT YEARWEEK("2017-06-15");
```

## MySQL高级函数

### BIN(x)

``` text
# 返回 x 的二进制编码
select DBINAY(15)
```

### BINARY(s)

``` text
# 将字符串 s 转换为二进制字符串
SELECT BINARY "RUNOOB";
```

### CASE expression WHEN condition1 THEN result1 ELSE result END cond

``` text
# CASE 表示函数开始，END 表示函数结束。如果 condition1 成立，则返回 result1, 如果 condition2 成立，
则返回 result2，当全部不成立则返回 result，而当有一个成立之后，后面的就不执行了。

SELECT
    CASE
    WHEN a.c = 1 THEN '1' ELSE '0' END CC
FROM (select 1 c) a
```

### CAST(x AS type)

``` text
# 转换数据类型
SELECT CAST("2017-08-29" AS DATE);
```

### COALESCE(expr1, expr2, ...., expr_n)

``` text
# 返回参数中的第一个非空表达式（从左向右）
SELECT COALESCE(NULL, NULL, NULL, 'rainsty', NULL, 'www.rainsty.com');
```

### CONNECTION_ID()

``` text
# 返回唯一的连接 ID
SELECT CONNECTION_ID();
```

### CONV(x,f1,f2)

``` text
# 返回 f1 进制数变成 f2 进制数
SELECT CONV(15, 10, 2);
```

### CONVERT(s USING cs)

``` text
# 函数将字符串 s 的字符集变成 cs
SELECT CHARSET(CONVERT('ABC' USING gbk))
```

### CURRENT_USER()

``` text
# 返回当前用户
SELECT CURRENT_USER();
```

### DATABASE()

``` text
# 返回当前数据库名
SELECT DATABASE();
```

### IF(expr,v1,v2)

``` text
# 如果表达式 expr 成立，返回结果 v1；否则，返回结果 v2。
SELECT IF(1 > 0,'正确','错误')
```

### IFNULL(v1,v2)

``` text
# 如果 v1 的值不为 NULL，则返回 v1，否则返回 v2。
SELECT IFNULL(null,'Hello Word')
```

### ISNULL(expression)

``` text
# 判断表达式是否为 NULL
SELECT ISNULL(NULL);
```

### LAST_INSERT_ID()

``` text
# 返回最近生成的 AUTO_INCREMENT 值
SELECT LAST_INSERT_ID();
```

### NULLIF(expr1, expr2)

``` text
# 比较两个字符串，如果字符串 expr1 与 expr2 相等 返回 NULL，否则返回 expr1
SELECT NULLIF(25, 25);
```

### SESSION_USER()

``` text
# 返回当前用户
SELECT SESSION_USER();
```

### SYSTEM_USER()

``` text
# 返回当前用户
SELECT SYSTEM_USER();
```

### USER()

``` text
# 返回当前用户
SELECT USER();
```

### VERSION()

``` text
# 返回当前数据库版本号
SELECT VERSION();
```
