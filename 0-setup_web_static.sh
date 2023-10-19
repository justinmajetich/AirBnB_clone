#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
# Install nginx
sudo apt-get update
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get -y install nginx
fi

if ! [ -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi

if ! [ -d /data/web_static/shared/ ]; then
    sudo mkdir -p /data/web_static/shared/
fi

index_html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

if ! [ -f /data/web_static/releases/test/index.html ]; then
    sudo touch /data/web_static/releases/test/index.html
    echo "$index_html" > /data/web_static/releases/test/index.html
fi

if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/


if ! grep -q "location /hbnb_static/ {" /etc/nginx/sites-available/default; then
    hostname=$(hostname)

    nginx_config=$(printf "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    server_name _;

    add_header X-Served-By %s;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /error_40x.html;
    location = /error_40x.html {
        root /var/www/error;
        internal;
    }
}" "$hostname")

    echo "$nginx_config" > /etc/nginx/sites-available/default
fi

if pgrep -x "nginx" > /dev/null
then
    sudo service nginx reload
else
    sudo service nginx start
fi
