#!/usr/bin/env bash
# Installs Nginx

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     add_header X-Served-By $HOSTNAME;
     root        /etc/nginx/html;
     index       index.html index.htm;

     location /hbnb_static {
         alias /data/web_static/current/;
         index index.html index.htm;
     }
}
" > /etc/nginx/sites-available/default

service nginx restart