#!/usr/bin/env bash

# install nginx if bit exiting in os
nb=$(which nginx | wc -l)
if [ $nb -eq 0 ]
then
    echo "nginx is not installed"
    echo "installation of the nginx server"
    #sudo apt-get update -y
    #sudo apt-get install nginx -y
else
    echo "nginx installé"
fi

echo "creation of directories"
sudo mkdir -p -v /data/web_static/releases/
sudo mkdir -p -v /data/web_static/shared/
sudo mkdir -p -v /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html