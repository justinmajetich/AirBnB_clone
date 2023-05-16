#!/usr/bin/env bash
# Set up server file system for deployment

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# configure file system
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# set permissions
sudo chown -R ubuntu:ubuntu /data/

# configure nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# restart web server
sudo service nginx restart
