#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   Json.py
@time:   2020-09-17 20:40:29
@description:
"""

import json
import pprint


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
