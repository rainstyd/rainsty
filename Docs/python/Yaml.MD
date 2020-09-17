* 导入模块  

``` python
import yaml
```

* 文件内容  

    [Yaml.py](../pythonFile/Yaml.py)

* 主要方法  

``` python
with open('./file/config.yml', 'r') as r:
    temp = yaml.load(r.read(), Loader=yaml.FullLoader)

print(temp)
```
