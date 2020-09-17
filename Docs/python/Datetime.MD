* 导入模块  

``` python
import time
import datetime
```

* 文件内容  

    [Datetime.py](../pythonFile/Datetime.py)

* 主要方法  

``` python
# 获取当前时间
now = datetime.datetime.now()
print(now)
print(type(now))

# 格式化时间为str
now = now.strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(type(now))

# 时间段转datetime
now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
print(now)
print(type(now))

# 日期计算
now = now + datetime.timedelta(days=10)
print(now)
print(type(now))

print(now.date())
print(now.time())
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 获取当前时间戳(s)
now = time.time()
print(now)
print(type(now))

# 时间戳转时间段(s)
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
print(now)
print(type(now))

# 时间段转时间戳(s)
now = time.mktime(time.strptime(now, '%Y-%m-%d %H:%M:%S'))
print(now)
print(type(now))
```
