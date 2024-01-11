#!/usr/bin/env bash
# bash script that sets up our webservers for deployment of web_static
# install nginx if it is not installed already
#   update package list
apt -y update 

#  install nginx
apt -y install nginx

# create folder /data/ and /data/web_static if it doesn't already exist
mkdir -p /data/web_static/

# create folder releases
mkdir -p /data/web_static/releases/

# create folder shared
mkdir -p /data/web_static/shared/

# create folder test
mkdir -p /data/web_static/releases/test

# create a fake HTML file
echo "Hello ALX thanks for this opportunity" > /data/web_static/releases/test/index.html

# creating symbolic link /data/web_static/current to /data/web_static/releases/test
ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving ownership of file to user ubuntu
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
config_str="\n\tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}"

sed -i "/server_name _;/a\ $config_str" /etc/nginx/sites-available/default


# enable new config by linking site-available with site-enabled 
ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled

# restarting nginx
service nginx restart
