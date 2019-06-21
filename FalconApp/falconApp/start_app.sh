#!/bin/bash

nohup gunicorn -w 1 -b 127.0.0.1:5000 falcon_manage:app > ./nohup.out 2>&1 &