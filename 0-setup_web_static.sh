#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt -y update

sudo apt install -y nginx
# Create the folder /data/web_static/releases/test/ if it doesn’t already exis
sudo mkdir -p /data/web_static/releases/test/
# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/
# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<h1>Static Test</h1>" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '53i\\t location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
