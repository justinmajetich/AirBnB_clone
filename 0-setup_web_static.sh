#!/usr/bin/env bash
#web_static development

#check for library updates
sudo apt-get -y update
sudo apt-get -y upgrade
#install nginx
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Konnichiwa! It's a test HTML file." | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
#permission setting
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
#restarting
sudo service nginx restart