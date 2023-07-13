#!/usr/bin/env bash
# This script sets up the web servers for deployment of web_static.

# Install Nginx if it's not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
folders=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        sudo mkdir -p "$folder"
    fi
done

# Create a fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
if [ -L "/data/web_static/current" ]; then
    sudo rm -f /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
# Remove any existing alias configuration
sudo sed -i '/alias \/hbnb_static\/ {/d' "$config_file"
sudo sed -i '/\t\talias \/data\/web_static\/current\/;$/d' "$config_file"
# Add new alias configuration
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' "$config_file"

# Restart Nginx
sudo service nginx restart

