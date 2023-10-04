#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static with nginx

# Check If nginx isn't installed
if ! dpkg -l | grep 'nginx' > /dev/null; then
  sudo apt-get update
  sudo apt-get -y install nginx
#  Check If nginx is running
  if ! pgrep -x nginx > /dev/null; then
    sudo service nginx start
  fi
fi

root="/data/web_static"
html="<html><head></head><body>Welcome Page!</body></html>"

# Checks if directories exists before creating them
if [ ! -d "$root" ]; then
  sudo mkdir -p "$root/releases/test"
  sudo mkdir -p "$root/shared"
  sudo chown -R "$USER":"$USER" "$root"
  echo "$html" | sudo tee "$root/releases/test/index.html" > /dev/null
  sudo ln -sf "$root/releases/test" "$root/current"
fi

nginx_cfg_loc="/etc/nginx/sites-available/default"
if ! grep '/hbnb_static/' "$nginx_cfg_loc" > /dev/null; then
  sudo sed -i "/server_name _;/a\\        location /hbnb_static/ {alias $root/current/;}" "$nginx_cfg_loc" > /dev/null
fi

sudo service nginx restart
