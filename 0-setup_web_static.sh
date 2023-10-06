#!/usr/bin/env bash
# Prepare web servers

#install nginx
apt-get update -y
apt-get install nginx -y

#create dirs and files
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Wills to the World yooo" > /data/web_static/releases/test/index.html

# create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data/

hbnb_static=$"\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sed -i '/^}$/i \ '"$hbnb_static" /etc/nginx/sites-available/default

apt install ufw -y
ufw allow 'NGINX HTTP'
service nginx restart
