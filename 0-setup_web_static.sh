#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
if [! -d /data/web_static/releases/test/]; then 
sudo mkdir  -p /data/web_static/releases/test/;
fi
echo "Testing" | sudo tee "/data/web_static/releases/test/index.html"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu "/data/"
sudo sed -i "\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx start
