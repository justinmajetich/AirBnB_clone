#!/usr/bin/env bash
#prep servers
path="/etc/nginx/sites-available/default"
fake="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "$fake" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/listen \[::\]:80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n}" $path
sudo service nginx restart
