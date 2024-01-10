#!/usr/bin/env bash
# Sets up an nginx web server
sudo su
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/ 
mkdir -p /data/web_static/shared/
echo "Hello World" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current 
chown -hR ubuntu:ubuntu /data/

content="
server {
        listen 80;

        location /hbnb_static {
					alias /data/web_static/current/
					index index.html
        }
}
events {}
"
echo "$content" > /etc/nginx/nginx.conf
service nginx start
