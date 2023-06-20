#!/usr/bin/env bash
# Installs Nginx if not installed
#+ Creates folders /data/web_static/shared
#+	and /adta/releases/test if not exists
#+ /data/web_static/current linked to
#+ /data/web_static/releases/test/
#+ Creates an /data/web_static/releases/test/index.html
#+ Configures Nginx to serve /data/web_static/current/ 
#+	to hbnb_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
