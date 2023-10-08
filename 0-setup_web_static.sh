#!/usr/bin/env bash
# This scripts Prepares the  web servers

#This will install nginx
apt-get update -y
apt-get install nginx -y

#This will create directorys and files...
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello Queensly Udongwo" > /data/web_static/releases/test/index.html

# create symbolic link for file
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data/

hbnb_static=$"\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sed -i '/^}$/i \ '"$hbnb_static" /etc/nginx/sites-available/default

apt install ufw -y
ufw allow 'NGINX HTTP'
service nginx restart
