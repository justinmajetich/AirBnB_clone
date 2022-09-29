#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
exit 0
