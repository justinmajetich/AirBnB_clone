#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

apt-get -y update > /dev/null 2>&1
apt-get -y install nginx > /dev/null 2>&1
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
TEST_INDEX=\
"<html>
    <head>
    </head>
    <body>
	Holberton School
    </body>
</html>"
echo "$TEST_INDEX" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/^server {/,/^}/!b;/^}/i\\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}' /etc/nginx/sites-enabled/default
nginx -s reload
