#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu: /data/

print %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	server_name _;
	add_header X-Served-By $HOSTNAME;

	location /hbnb_static/ {
		alias /data/web_static/current/hbnb_static/;
		index index.html;
	}
}" > /etc/nginx/sites-enabled/default

service nginx restart
