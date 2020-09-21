#!/bin/bash

## The script installs docker-engine, its components as well as docker-compose


# Docker is installed as a root.
if [ "${USER}" != "root" ]; then
    echo "$0 must be run as root!"
    exit 2
fi


yum check-update
yum -y install wget


## Checks if docker is installed or not. To avoid high installation time.

command -v docker > /dev/null 2>&1 || { 

	echo ">> INSTALLING DEPENDENCIES <<"

	echo ">> STEP 1 ----- INSTALLING DOCKER <<"

	curl -fsSL https://get.docker.com/ | sh

	systemctl start docker

	echo ">> STEP 2 ----- INSTALLING DOCKER-COMPOSE <<" 

	curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

	sudo mv /usr/local/bin/docker-compose /usr/bin/docker-compose

	chmod +x /usr/bin/docker-compose

}

