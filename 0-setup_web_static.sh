#!/usr/bin/env bash
# Preparing your web servers

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
FAKEHTMLFILE="/data/web_static/releases/test/index.html"
sudo echo "Holberton" >> "$FAKEHTMLFILE"
symbolic="/data/web_static/current"
rm -f "$symbolic"
sudo rm -f "/data/web_static/releases/test/current"
sudo ln -s "$symbolic" /data/web_static/releases/test/
sudo chown -hR ubuntu:ubuntu /data/
FILE="/etc/nginx/sites-available/default"
ALIAS="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "47i\ $ALIAS" "$FILE"
service nginx restart
