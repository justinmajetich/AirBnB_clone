#!/usr/bin/env bash
#  sets up your web servers for the deployment
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/releases/test

sudo touch /data/web_static/releases/test/index.html

sudo echo "
<html>
    <head>
    </head>
        <body>
        Holberton School
        </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data
file="/etc/nginx/sites-available/default"
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' $file

sudo service nginx restart
