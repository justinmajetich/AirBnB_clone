#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
echo '<h1>hello world, this is a test</h1>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '11i alias /data/web_static/current/;' /etc/nginx/sites-available/default
sudo service nginx restart
