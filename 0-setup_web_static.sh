#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y nginx
# Create directories...
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

# create index.html for test directory
echo "<h1>Welcome to kiranga.tech <\h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# give user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# Set-up the content of /data/web_static/current/ to redirect
# to domain.tech/hbnb_static
sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
