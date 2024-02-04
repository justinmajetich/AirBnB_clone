#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

#ommands update the package lists and install Nginx, a web server software

apt-get -y update > /dev/null
apt-get install -y nginx > /dev/null

# Create all necessary directory structure required for the deployment of the static website.
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello World again!" > /data/web_static/releases/test/index.html

# Check if directory current exist
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi
# Create a symbolic link to test
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to user ubuntu
chown -hR ubuntu:ubuntu /data

# Configure nginx to serve content pointed to by symbolic link to hbnb_static
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart server
service nginx restart
