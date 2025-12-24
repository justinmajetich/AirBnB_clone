#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! command -v nginx;
then
    echo "Nginx is not installed. Installing..."
    apt-get update
    apt-get install nginx -y
    service nginx start

else
    echo "Nginx is already installed. Skipping installation."
fi

# Create necessary parent directories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Creating symbolic links
ln -sf /data/web_static/releases/test/ /data/web_static/current

# create sample pages
echo "Holberton School" > /data/web_static/releases/test/index.html

# Adjust the permissions or ownership of the folders
chown -R ubuntu:ubuntu /data/
chmod -R 755 /data/

# sudo ln -s "/etc/nginx/sites-available/default" "/etc/nginx/sites-enabled/"
# Creating Server Block Files
sed -i '49i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# If no problems were found, restart Nginx to enable your changes
nginx -t
service nginx restart
