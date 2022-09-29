#!/usr/bin/env bash
#Bash script that sets up web servers for the deployment of web_static.

sudo apt-get update

#install nginx
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello web server" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
