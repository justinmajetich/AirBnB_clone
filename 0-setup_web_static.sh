#!/usr/bin/env bash
# Script to configure the web server to serve web-static
sudo apt-get update
sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'

if [ ! -d /data/ ]; then
	sudo mkdir /data/
fi
if [ ! -d /data/web_static/ ]; then
	sudo mkdir /data/web_static/
fi
if [ ! -d /data/web_static/releases ]; then
	sudo mkdir /data/web_static/releases/
fi
if [ ! -d /data/web_static/shared/ ]; then
	sudo mkdir /data/web_static/shared/
fi
if [ ! -d /data/web_static/releases/test/ ]; then
	sudo mkdir /data/web_static/releases/test/
fi
str=\
"
<html>
<head>
</head>
<body>
   Holberton School
</body>
</html>
"
if [ ! -f /data/web_static/releases/test/index.html ]; then
	echo "$str" > /data/web_static/releases/test/index.html
fi
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
	ln -s /data/web_static/releases/test/ /data/web_static/current
else
	ln -s /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}" /etc/nginx/sites-enabled/default

sudo service nginx restart
