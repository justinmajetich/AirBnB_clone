#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt update && sudo apt install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
directory=/data/web_static/current
if [[ -d $directory ]]
then
	sudo rm -r /data/web_static/current
	ln -sf /data/web_static/releases/test $directory
else
	ln -sf /data/web_static/releases/test $directory
fi
chown -R ubuntu /data/
chgrp -R ubuntu /data/
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	index index.html index.htm;

	location /hbnb_static{
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 http://cuberule.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default
service nginx restart


