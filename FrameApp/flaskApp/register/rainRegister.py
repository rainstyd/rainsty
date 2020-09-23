# -*- coding: utf-8 -*-
import requests
import json


def register(self):
    url = 'http://127.0.0.1:8001/rainenrollment'
    headers = {
        'Content-Type': 'application/json'
    }
    req = requests.post(url=url, data=json.dumps(self), headers=headers)
    print(req.status_code)
    return req.text


if __name__ == '__main__':
    info = {"username": "rainsty", "password": "xxxxxxxxxxxxx"}
    result = register(info)
    print(result)
