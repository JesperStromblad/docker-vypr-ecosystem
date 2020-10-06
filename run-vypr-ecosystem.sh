#!/usr/bin/env bash

# This script sets up docker container and container services for web tool.
# TODO: write some instructions about the architecture of the containers configured for web tool

printf "\033[0;31m Building and running container for analysis environment \033[0m \n"

# We first build Analysis environment
docker build -f Dockerfile_vypr -t vypr .
#
## We run it in detached mode
docker run -d -p 9002:9002 vypr


# Visualisation tool works by first setting up verdict server in docker container and visualization tool runs on host machine

# Synchronizing container with the host's timezone
TZ=`date +%Z`

if [ $TZ == 'CEST' ] ; then 
     TZ='CET'
fi
echo $TZ

docker build -f server/Dockerfile -t verdict .
docker run -d -p 9003:9003 -e TZ=$TZ verdict


bash ./client-script.sh 




printf "\033[0;31m IMPORTANT INSTRUCTIONS:  \033[0m \n"
printf "\033[0;31m Container for analysis environment completed. \033[0m \n"
printf "\033[0;31m Use http://localhost:9002/ on your browser for analysis environment \033[0m \n"
#
printf "\n\n"

printf "\033[0;31m Container Services for visualization completed. \033[0m \n"
printf "\033[0;31m Use http://localhost:9001/ on your browser for Visualization environment \033[0m \n"




docker build -q -f Dockerfile_jupyter -t vyprjupyter .
docker run -p 9005:9005 vyprjupyter
