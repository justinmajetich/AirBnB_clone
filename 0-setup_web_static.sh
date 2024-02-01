#!/usr/bin/env bash
# Setting up my web servers

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'HTTP Nginx'

touch -p /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared

ln -sf /data/web_static/current /data/web_static/releases/test/

chown -R ubuntu:ubuntu /data/