#!/usr/bin/env bash                                                                                             
# Bash script that sets up your web servers for the deployment of web_static                                    

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '40 a\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n ' /etc/nginx/sites-avai\
lable/default

sudo service nginx restart
