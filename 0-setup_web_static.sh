#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

apt-get update -y > /dev/null/;
apt-get install -y nginx > /dev/null/;
apt-get upgrade -y > /dev/null/;

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

  location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
  }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
