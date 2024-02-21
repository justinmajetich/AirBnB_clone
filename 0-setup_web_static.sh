#!/usr/bin/env bash
# Configires Nginx server with deploymeny folders
apt-get update -y
apt-get install -y nginx
mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "<marquee> Let's get it </marquee>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
# Write after the error declaration
sed -i "/error_page 404 \/404.html;/a \\\n\tlocation /hbnb_static { \
        \n\t\talias /data/web_static/current/; \
        \n\t\tautoindex off; \
        \n\t}" /etc/nginx/sites-available/default
# restart nginx
service nginx restart
