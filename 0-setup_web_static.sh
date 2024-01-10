#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi


sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
    add_header X-Served-By $hostname;
}" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
