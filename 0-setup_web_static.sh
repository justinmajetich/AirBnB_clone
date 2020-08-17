#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get install -y nginx
sudo ufw allow "Nginx HTTP"

# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file, with simple content, to test your Nginx configuration
printf %s "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
" > /data/web_static/releases/test/index.html

# Create a symbolic link,If the symbolic link already exists, it should be deleted and recreated every time the script is ran.

ln -sf /data/web_static/releases/test/ /data/web_static/current
# Recursively Change the File Ownership
chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "/listen 80 default_server;/ \\\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
# Nginx restart after updating the configuration
sudo service nginx restart
