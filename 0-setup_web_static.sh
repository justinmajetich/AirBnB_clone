#!/usr/bin/env bash
# script that configures a Nginx server
# 	- create folders
#	- create a fake HTML file
#	- create a symbolic link linked to test folder
#	- change the ownership of the /data/ folder
#	- use Alias in the configuration file

# update apt-get
apt-get update

# install nginx if it is not already installed
if [[ ! ("$(sudo which nginx)") ]]; then
	apt-get install -y nginx
fi

# mmake necessary folders and config changes
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Ceci n'est pas une page" > /var/www/html/404.html
printf "%s" "<!DOCTYPE html>
<html>
    <head>
        <title>Test HTML document</title>
    </head>
    <body>
        <p>This is a test file</p>
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
echo "location /hbtn_static {
      alias /data/web_static/current/;
}" >> /etc/nginx/sites-available/default
printf "%s" "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
    location /hbtn_static {
      alias /data/web_static/current/
    }
}" > /etc/nginx/sites-available/default
