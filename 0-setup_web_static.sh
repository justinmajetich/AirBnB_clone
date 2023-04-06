#!/usr/bin/env bash
# This script prepares nginx to serve a static web page
# Install Nginx if it's not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update > /dev/null
    sudo apt-get install -y nginx > /dev/null
fi

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared > /dev/null

# Create a fake HTML file for testing
echo "<html><head><title>Test</title></head><body><p>This is a test</p></body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update the symbolic link
sudo rm -f /data/web_static/current > /dev/null
sudo ln -s /data/web_static/releases/test /data/web_static/current > /dev/null

# Set ownership of the directories to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/ > /dev/null

# Update Nginx configuration
sudo sed -i '/server {/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart > /dev/null

# Exit successfully
exit 0
