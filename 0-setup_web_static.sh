#!/usr/bin/env bash
#sets up a web server for deployment of web_static
sudo apt update -y
sudo apt install nginx -y
sudo mkdir -pv /data/web_static/releases/test/
sudo mkdir -pv /data/web_static/shared/
sudo echo "Hello World!" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
echo "
server {
  listen 80;
  listen [::]:80 default_server;
  location /hbnb_static {
    alias /data/web_static/current/;
  }
  index index.html;
  server_name ebukaejie.tech;
  rewrite '^/redirect_me$' http://example.com permanent;
  error_page 404 /custom_404.html;
  add_header X-Served-By $HOSTNAME;
}" | sudo tee -a /etc/nginx/sites-available/default
sudo service nginx restart
