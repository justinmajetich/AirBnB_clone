#!/usr/bin/env bash
# Set up a web servers for the deployment of `web_static`

# Install Nginx if it not already installed
if ! [ -x  "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get install nginx -y
fi
# Creates /data/ if it doesn’t already exist
if ! [ -d /data/ ]; then
	mkdir /data/
fi
# Creates /data/web_static/ if it doesn’t already exist
if ! [ -d /data/web_static/ ]; then
	mkdir -p /data/web_static/
fi
# Creates /data/web_static/releases/ if it doesn’t already exist
if ! [ -d /data/web_static/releases/ ]; then
	mkdir -p /data/web_static/releases/
fi
# Creates /data/web_static/shared/ if it doesn’t already exist
if ! [ -d /data/web_static/shared/ ]; then
	mkdir -p /data/web_static/shared/
fi
# Creates /data/web_static/releases/test/ if it doesn’t already exist
if ! [ -d /web_static/releases/test/ ]; then
	mkdir -p /data/web_static/releases/test/
fi
# Creates a fake HTML file /data/web_static/releases/test/index.html
# Creates a symbolic link /data/web_static/current linked to the
sudo bash -c 'cat <<EOT > /data/web_static/releases/test/index.html
<html>
 <head>
 </head>
 <body>
   Best School
 </body>
</html>
EOT'
# /data/web_static/releases/test/ folder.
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
# Giving ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Updates the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
sudo sed -i "/^server {/a \\
	location /hbnb_static { \\
	alias /data/web_static/current/; \\
}" /etc/nginx/sites-available/default

sudo service nginx restart
