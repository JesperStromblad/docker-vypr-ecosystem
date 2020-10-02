#!/usr/bin/env bash


# IMPORTANT: This file is dangerous if you have many containers unrelated to web-tool.
# We will provide a different mechanism for automatic cleanup of specific containers

# Stop all containers
docker stop $(docker ps -a -q)

# Remove all containers
docker rm $(docker ps -a -q)


# This cleans up python process
PID=`ps aux | grep python | grep -v grep | awk '{print $2}'`

# Loop for process ids to kill python processes.
for pid in $PID
do 
	kill -9 $pid
done

