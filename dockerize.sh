#!/bin/bash

docker build .

ID=$(docker images |grep none|awk '{print $3}')

echo "docker image id: $ID"

docker tag $ID zsy9docker/ecg-flask

docker push zsy9docker/ecg-flask