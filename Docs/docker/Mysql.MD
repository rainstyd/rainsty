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

### FORMAT(x,n)  

``` text
# 函数可以将数字 x 进行格式化 "#,###.##", 将 x 保留到小数点后 n 位，最后一位四舍五入。
select FORMAT(52.131400, 4)
```

### AAA  

``` text
# AAAAAA
select AAA()
```

### AAA  

``` text
# AAAAAA	
select AAA()
```

### AAA  

``` text
# AAAAAA	
select AAA()
```

### AAA  

``` text
# AAAAAA		
select AAA()
```
