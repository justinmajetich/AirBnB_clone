#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 2 'Nginx HTTP'
sudo mkdir /data/web_static/releases/test/
echo "<html>
    <head>
    </head>
    <body>
        Hello school
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo servvice nginx restart
exit 0