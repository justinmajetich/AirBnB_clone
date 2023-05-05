#!/usr/bin/env bash
# This script prepares nginx webserver to host a static site
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared /data/web_static/current

# Create a fake HTML file for testing Nginx configuration
echo "<html><head><title>Test HTML file</title></head><body><p>This is a test HTML file.</p></body></html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/
if ! grep -q "location /hbnb_static/ {" /etc/nginx/sites-available/default
then
    sudo sed -i '/^\tserver_name localhost;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
fi

# Restart Nginx
sudo service nginx restart

exit 0
