#! /bin/bash
xhost +local:root
docker-compose -f docker-compose-nvidia.yaml up