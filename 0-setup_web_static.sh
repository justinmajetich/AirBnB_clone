#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Welcome to AirBnB" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
serve="\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sed -i "s/^\tserver_name .*;$/&\n$serve/" /etc/nginx/sites-available/default
sudo service nginx restart
