#!/usr/bin/env bash


# IMPORTANT: This file is dangerous if you have many containers unrelated to web-tool.
# We will provide a different mechanism for automatic cleanup of specific containers

# Stop all containers
docker stop $(docker ps -a -q)

# Remove all containers
docker rm $(docker ps -a -q)
