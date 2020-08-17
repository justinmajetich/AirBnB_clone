#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# Install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create test html file
direct="/data/web_static/releases/test/index.html"
echo -e """
    <html>
        <body>
            Holberton School
        </body>
    </html>
""" | sudo tee $direct

# Create sym link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give owner of the /data/ folder to ubuntu user and groups
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static (https://mydomainname.tech/hbnb_static)
config_file="/etc/nginx/sites-available/default"
sudo sed -i '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file

# restart server
sudo service nginx restart
