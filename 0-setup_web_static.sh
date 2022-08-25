#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

apt-get update -y;
apt-get install -y nginx;

mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;

ln -sf /data/web_static/releases/test/ /data/web_static/current

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

  location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
  }

  location /redirect_me {
    return 301 https://i.imgur.com/guDXtsC.png;
  }
}
" > /etc/nginx/sites-available/default

sudo service nginx restart
