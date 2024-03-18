#!/usr/bin/env bash
#setup server with configurations

sudo apt-get -y update
sudo apt install -y nginx

#create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#create symbolic link
sudo ln -sTf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/
sudo service nginx restart

#cp /etc/nginx/sites-enabled/default www/data/web_static/current/

#configure nginx locations path

NGINX_CONFIG_FILE="/etc/nginx/sites-available/default"
STATIC_CONTENT_PATH="/data/web_static/current/"
DOMAIN_NAME="bellacocho.tech"

if ! grep -q "location /hbnb_static" "$NGINX_CONFIG_FILE"; then
	sudo sed -i '/server_name '"$DOMAIN_NAME"';/a \        location /hbnb_static {\n            alias '"$STATIC_CONTENT_PATH"';\n        }' "$NGINX_CONFIG_FILE"
else
	sudo sed -i 's@location /hbnb_static.*$@location /hbnb_static {\n            alias '"$STATIC_CONTENT_PATH"';\n        }@' "$NGINX_CONFIG_FILE"
fi

sudo service nginx restart
