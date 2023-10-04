#!/usr/bin/env bash
# script to sets up your web servers for the deployment of web_static

# update linux
apt-get update
#install nginx
apt-get install -y nginx

# create folder 'data'
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create a dummy content
echo 'This is Naziff website' > /data/web_static/releases/test/index.html

# symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership and group
chown -R ubuntu /data/ && chgrp -R ubuntu /data/

# configure server
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://naziff.tech/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# restart nginx
service nginx restart
