* 导入模块  

``` python
import configparser
import codecs
import chardet
```

* 文件内容  

    [Configparser.py](../pythonFile/Configparser.py)
    [config.ini](../pythonFile/file/config.ini)

* 主要方法  

``` python
config_file = './file/config.ini'
conf = configparser.ConfigParser()

# 获取文件编码
with open(config_file, 'rb') as rb:
    code = chardet.detect(rb.read())

print(code)

# 以获取到的编码打开文件
with codecs.open(config_file, 'r', encoding=code['encoding']) as r:
    conf.read_file(r)

# 读取配置文件内容
sections = conf.sections()
print(sections)
config = dict(conf.items('config'))
print(config)
```
