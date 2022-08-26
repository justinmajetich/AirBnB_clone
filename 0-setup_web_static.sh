#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

apt-get update -y;
apt-get install -y nginx;

mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;

#rm -fr /data/web_static/current > /dev/null/;
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -fs /data/web_static/releases/test /data/web_static/current

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

  location    /redirect_me {
      return 301 http://yourdomaindesign.tech/redirect_me;
  }

  location = /404.html {
    root /etc/nginx/html;
    internal;
  }
}" >/etc/nginx/sites-available/default

sudo service nginx restart
