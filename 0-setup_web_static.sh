#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Install Nginx if it's not already installed
if [ $(dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -c "ok installed") -eq 0 ]; then
  sudo apt-get update
  sudo apt-get install nginx -y
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and of /data/ folder
sudo chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu /data/

# backup default server config file
# sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

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
        return 301 https://github.com/chineduCoded;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
