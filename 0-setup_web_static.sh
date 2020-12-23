#!/usr/bin/env bash
#web servers for the deployment 

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "create files" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "/^\tlocation \/ {$/ i\\location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
service nginx restart
