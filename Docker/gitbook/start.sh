#!/bin/bash

# cd ../rainsty && git pull origin master && cd ../gitbook
# cp -r ../rainsty/Docs/* ./gitbook/

# mkdir gitbook
# cp -r ../../Docs/* ./gitbook/

docker network create rainsty
docker-compose up -d
docker-compose restart
