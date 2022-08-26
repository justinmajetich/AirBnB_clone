#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

apt-get update -y;
apt-get install -y nginx;

mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;
touch /data/web_static/releases/test/index.html;

rm -fr /data/web_static/current;
ln -fs /data/web_static/releases/test /data/web_static/current
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /etc/nginx/html;
  index index.html;
  error_page 404 /custum_404.html;

  location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
  }

  location = /custum_404.html {
    root /etc/nginx/html;
    internal;
  }

  location /redirect_me {
    return 301 https://i.imgur.com/guDXtsC.png;
  }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
