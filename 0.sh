#!/usr/bin/env bash
#install nginx

sudo apt -y update
sudo apt-get -y install nginx
sudo ufw app list
sudo ufw allow 'Ngnix HTTP'
sudo ufw disable
sudo ufw status
sudo apt-get install curl
curl -4 icanhazip.com
sudo systemctl start nginx
sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

printf %s "server {
        listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;
        
	location /hbnb_static {
		alias /data/web_static/current;
	        index index.html index.htm;
	}

	location /redirect_me {
		return 301 https://youtu.be/eaW0tYpxyp0.com;
	}
	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
	        internal;
	}
}" > /etc/nginx/sites-available/default

sudo systemctl restart nginx
