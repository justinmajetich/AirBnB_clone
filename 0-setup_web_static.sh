#!/usr/bin/env bash
# This script that configures a physical server using the  Nginx server.

# update apt-get
sudo apt-get -y update

# install nginx if it is not already installed
if [[ ! ("$(sudo which nginx)") ]]; then
	sudo apt-get -y install nginx
fi

sudo ufw allow 'Nginx HTTP'

# Create folders and make necessary folders and config changes
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Ceci n'est pas une page" > /var/www/html/404.html

INDEX_CONTENT="<h1>bovntyhvnter.tech test file</h1>"
echo "$INDEX_CONTENT" > /data/web_static/releases/test/index.html

#--prevent overwrite
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;

# Create a symbolic link linked to test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change the ownership of the /data/ folder
sudo chown -hR ubuntu:ubuntu /data/

# Set up and use alias in server configuration file
SERVER_CONFIG=\
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$hostname;
    root   /var/www/html;
    index  index.html index.htm index.nginx-debian.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404.html {
      root /var/www/html;
      internal;
    }
    location /hbnb_static {
      alias /data/web_static/current/;
    }
}"

echo -e "$SERVER_CONFIG" > /etc/nginx/sites-available/default

# Symbolically link sites-available to sites-enabled
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# Start server if server not started else restart
if [ "$(pgrep -c nginx)" -le 0 ]; then
    service nginx start
else
    service nginx restart
fi
