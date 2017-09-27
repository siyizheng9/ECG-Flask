#!/bin/bash

docker build .

TAG='zsy9docker/ecg-flask'

ID=$(docker images |grep none|awk '{print $3}')

echo "\nnew generated docker image id: $ID\n"

docker tag $ID $TAG

docker push $TAG