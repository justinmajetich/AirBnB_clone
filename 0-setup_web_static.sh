#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -intall nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Hello Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
