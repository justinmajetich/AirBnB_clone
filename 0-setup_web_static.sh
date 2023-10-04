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
  sudo chown -R "$USER":"$USER" "$root"
  sudo mkdir -p "$root/shared"
  echo "$html" | sudo tee "$root/releases/test/index.html" > /dev/null
  sudo ln -sf "$root/releases/test" "$root/current"
fi

sudo sed -i "37i \\\tlocation /hbnb_static/ {\n\t\talias $root/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart
