#!/usr/bin/env bash

docker build -t doc-rotary --file ./Dockerfile .
docker kill doc-rotary || "already killed"
docker rm doc-rotary || "already removed"
echo "running..."
echo "docker run -p 127.0.0.1:8888:80 -e PORT=80 --name doc-rotary doc-rotary"

docker run -p 127.0.0.1:8888:80 -e PORT=80 --name doc-rotary doc-rotary