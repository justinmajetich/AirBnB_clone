#!/usr/bin/env bash
# Prepare your web servers

## Update server
sudo apt-get -y update
sudo apt-get -y upgrade

## Install NGINX
sudo apt-get -y install nginx

## Creates directories
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test

## Write Hello World in index with tee command
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

## Create Symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

## Change owner and group like ubuntu
sudo chown -R ubuntu:ubuntu /data

## Add new configuration to NGINX
sudo sed -i "/listen 80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

## Restart NGINX
sudo service nginx restart
