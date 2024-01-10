#!/usr/bin/env bash
# Update, upgrade, and install Nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
# Create directories and index.html file
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Change ownership
sudo chown -hR ubuntu:ubuntu /data/
# Configure Nginx
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart Nginx
sudo service nginx restart
