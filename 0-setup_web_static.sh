#!/usr/bin/env bash
<<<<<<< HEAD
# Preparing your web servers

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
FAKEHTMLFILE="/data/web_static/releases/test/index.html"
sudo echo "Holberton" >> "$FAKEHTMLFILE"
symbolic="/data/web_static/current"
rm -f "$symbolic"
sudo rm -f "/data/web_static/releases/test/current"
sudo ln -s "$symbolic" /data/web_static/releases/test/
sudo chown -hR ubuntu:ubuntu /data/
FILE="/etc/nginx/sites-available/default"
ALIAS="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "47i\ $ALIAS" "$FILE"
=======
#set up your web servers for the deployment of web_static

apt-get update -y
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
ln -sf /data/web_static/releases/test/ /data/web_static/current
echo 'Hello there!!!' > /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data/
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm index.nginx-debian.html;
    server_name _;
	    
    location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html index.htm;
	autoindex off;
	}	
	location /redirect_me {
	return 301 http://graceeffiong.tech;
	}
	error_page 404 /404.html;
	location /404 {
	root /var/www/error;
	internal;
	    }
}" > /etc/nginx/sites-available/default
>>>>>>> 59eb11dc411dd639fa925755cc636f2eb449d3a8
service nginx restart
