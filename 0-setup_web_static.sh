#!/usr/bin/env bash
#Script that sets up your web servers for the deployment of web_static

if ! dpkg -s nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir -p /data/web_static/releases/test

html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$html" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo rm -rf /data/web_static/current || true
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data


sudo wget -q -O /etc/nginx/sites-available/default http://exampleconfig.com/static/raw/nginx/ubuntu20.04/etc/nginx/sites-available/default
config="/etc/nginx/sites-available/default"
echo 'Holberton School' | sudo tee /var/www/html/index.html > /dev/null
sudo sed -i '/^}$/i \ \n\tlocation \/redirect_me {return 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;}' $config
sudo sed -i '/^}$/i \ \n\tlocation @404 {return 404 "Ceci n'\''est pas une page\\n";}' $config
sudo sed -i 's/=404/@404/g' $config
sudo sed -i "/^server {/a \ \tadd_header X-Served-By $HOSTNAME;" $config
sudo sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config

service nginx restart
