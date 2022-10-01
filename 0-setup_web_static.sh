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

sudo rm -rf /data
echo "creation of directories"
sudo mkdir -p -v /data/web_static/releases/
sudo mkdir -p -v /data/web_static/shared/
sudo mkdir -p -v /data/web_static/releases/test/
echo "Hello World Nginx" > index.html
sudo mv index.html /data/web_static/releases/test/
cat /data/web_static/releases/test/index.html

echo "creation of the symbolic link"
sudo rm /data/web_static/current
sudo ln -s -v /data/web_static/releases/test/ /data/web_static/current

echo "Give ownership of the /data/ folder to the ubuntu user AND group"
