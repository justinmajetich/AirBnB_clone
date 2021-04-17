#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
printf "<html>\n\t<head></head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/listen 80 default_server;/a location /hbnb_static {\\n\\talias /data/web_static/current/;\\n\\t}\\n" /etc/nginx/sites-available/default
sudo service nginx restart
