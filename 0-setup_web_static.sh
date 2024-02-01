#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

if ! dpkg -l nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories and files
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link if it doesn't exist or update if exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership
sudo chown -R root:root /data/

# Update Nginx configuration to serve content of /data/web_static/current to hbnb_static
config_file="/etc/nginx/sites-available/default"
if grep -q "location /hbnb_static" "$config_file"; then
    sudo sed -i 's/location \/hbnb_static {/location \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;/' "$config_file"
else
    sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$config_file"
fi

sudo service nginx restart

exit 0
