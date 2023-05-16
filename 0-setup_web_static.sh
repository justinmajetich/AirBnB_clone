#!/usr/bin/env bash
# Configure a web server for web static deployment
# Install and configure Nginx if it doesn't already exist
sudo apt-get update
sudo apt-get install -y nginx

# Create the folders for deployment
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file with simple content
echo "Holberton School" | sudo tee -a /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# set permissions
sudo chown -R ubuntu:ubuntu /data/

# configure nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
