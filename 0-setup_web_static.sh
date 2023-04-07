#!/usr/bin/env bash
# Bash script that sets up web servers for the development of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Ngnix HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/release/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/release/test/
sudo touch /data/web_static/release/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
   Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static {alis /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart 
