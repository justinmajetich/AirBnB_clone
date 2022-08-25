#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

apt-get update -y;
apt-get install -y nginx;

mkdir -p /data/web_static/releases/;
mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;
touch -p /data/web_static/releases/test/index.html;
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html;

sudo ln -sf /data/web_static/current /data/web_static/releases/test/;
sudo chown -R ubuntu /data/

printf %s "server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /data/web_static/current;
  index index.html;

  location /static {
    alias /hbnb_static/;
  }
}
" >> /etc/nginx/sites-available/default;

sudo service nginx restart
