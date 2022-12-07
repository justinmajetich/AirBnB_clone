#!/usr/bin/env bash
# Set up web servers to deploy web_static

apt update
apt -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
echo "Fake file" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '47i\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default
service nginx restart
