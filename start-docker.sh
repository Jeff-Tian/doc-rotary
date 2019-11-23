#!/usr/bin/env bash

docker build -t bitq --file ./Dockerfile .
docker kill bitq || "already killed"
docker rm bitq || "already removed"
echo "running..."
echo "docker run -p 127.0.0.1:8888:80 -e PORT=80 --name bitq bitq"

docker run -p 127.0.0.1:8888:80 -e PORT=80 --name bitq bitq