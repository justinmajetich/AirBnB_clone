#!/usr/bin/env bash
# Sets up an nginx web server
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/ 
sudo mkdir -p /data/web_static/shared/
echo "Hello World" | sudo tee -a  /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -hR ubuntu:ubuntu /data/

content="
http {
	server {
					listen 80;

					location /hbnb_static {
						alias /data/web_static/current/;
						index index.html;
					}
	}
}
events {}
"
echo "$content" | sudo tee /etc/nginx/nginx.conf
sudo service nginx start
