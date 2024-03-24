#!/usr/bin/env bash
# Sets up web servers for the deployment of `web_static`

if command -v nginx &> /dev/null; then
  echo "Nginx already installed."
else
  apt-get update
  apt-get install -y nginx
fi

# Create necessary files
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Best School" > /data/web_static/releases/test/index.html

# Recreate symlink every run
if [ -L /data/web_static/current ]; then
  echo "Symoblic link exists. Deleting..."
  rm -f /data/web_static/current
fi
echo "Creating symoblic link..."
ln -s /data/web_static/releases/test/ /data/web_static/current


# Give permissions to user and group `ubuntu`
chown -R ubuntu:ubuntu /data/

# Update nginx to serve content correctly
sed -i '/server_name _;/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tindex index.html index.htm;\n\t}' /etc/nginx/sites-available/default
# Restart nginx
service nginx restart
