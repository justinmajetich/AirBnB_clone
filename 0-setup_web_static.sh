#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' /etc/nginx/sites-available/default

service nginx restart
