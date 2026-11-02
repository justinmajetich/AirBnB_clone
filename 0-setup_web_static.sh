#!/usr/bin/env bash
#A Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

#adding a test string

echo "Welcome to my server" | sudo tee /data/web_static/releases/test/index.html

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        error_page 404 /404.html;
        location = /404.html {
                internal;
        }
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        location /hbnb_static {
                alias /data/web_static/current/;
        }

}" | sudo tee /etc/nginx/sites-available/default
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo rm -rf /etc/nginx/sites-enabled
sudo ln -sf /etc/nginx/sites-available/ /etc/nginx/sites-enabled
sudo chown -hR ubuntu:ubuntu /data
sudo service nginx restart
