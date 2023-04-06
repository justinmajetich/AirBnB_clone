#!/usr/bin/env bash
#nginx automate config
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<h1>HELLO WORLDDDD</h1>" > /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server;/a\\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart

