#!/usr/bin/env bash
# Script using bash to setup webservers for deployment of simple HTML
# content

apt-get update && \
apt-get install -y nginx && \
mkdir -p -m=755 /data/web_static/{releases/test,shared} || exit 0
echo 'Testing 123' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
insert='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}'
sed -i "37i $insert" /etc/nginx/sites-available/default
service nginx restart
exit 0
