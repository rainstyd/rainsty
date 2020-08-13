#!/bin/bash

docker network create rainsty
docker-compose up -d
docker-compose restart
