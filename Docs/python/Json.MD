* 导入模块  

``` python
import json
import pprint
```

* 文件内容  

    [Json.py](../pythonFile/Json.py)

* 主要方法  

``` python
d = {
    'version': '2.0',
    'services': {
        'python': {
            'image': 'python:3.6.5',
            'restart': 'always',
            'hostname': 'python',
            'container_name': 'python',
            'environment': {'TZ': 'Asia/Shanghai'},
            'volumes': [
                './volumes/run.sh:/run.sh',
                './volumes/requirements.txt:/requirements.txt',
                './volumes/file:/file'],
            'command': 'bash /run.sh',
            'networks': ['rainsty']
        }
    },
    'networks': {
        'rainsty': {
            'external': {
                'name': 'rainsty'
            }
        }
    }
}


j = json.dumps(d)
print(j)

j = json.dumps(d, ensure_ascii=False, indent=4)
print(j)


s = """
{
    "version": "2.0",
    "services": {
        "python": {
            "image": "python:3.6.5",
            "restart": "always",
            "hostname": "python",
            "container_name": "python",
            "environment": {
                "TZ": "Asia/Shanghai"
            },
            "volumes": [
                "./volumes/run.sh:/run.sh",
                "./volumes/requirements.txt:/requirements.txt",
                "./volumes/file:/file"
            ],
            "command": "bash /run.sh",
            "networks": [
                "rainsty"
            ]
        }
    },
    "networks": {
        "rainsty": {
            "external": {
                "name": "rainsty"
            }
        }
    }
}
"""

j = json.loads(s)
pprint.pprint(j)
```
