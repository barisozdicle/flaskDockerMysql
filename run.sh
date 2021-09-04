#!/usr/bin/env bash

docker build -t mysql -f ./build/Dockerfile.mysql .
docker build -t python -f ./build/Dockerfile.python .
docker-compose up -d
