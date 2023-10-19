#!/usr/bin/env bash

# Install nginx
sudo apt-get update
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get -y install nginx
fi

if ! [ -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi

if ! [ -d /data/web_static/shared/ ]; then
    sudo mkdir -p /data/web_static/shared/
fi

index_html="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

if ! [ -f /data/web_static/releases/test/index.html ]; then
    sudo touch /data/web_static/releases/test/index.html
    echo "$index_html" | sudo tee /data/web_static/releases/test/index.html
fi

if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

if ! grep -q "location /hbnb_static/ {" /etc/nginx/sites-available/default; then
    sudo sed -i "38i\ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
fi

sudo service nginx restart
