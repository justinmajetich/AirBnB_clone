#!/usr/bin/env bash
# This is a bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# To create folders
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create a file index.html
sudo touch /data/web_static/releases/test/index.html

# to create content inside index.html
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# To create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# To give ownership of /data/ folder to ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# To configure nginx to server the content

replace='# pass PHP scripts to FastCGI server'

content='location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'

sudo sed -i "s|$replace|$content|g" /etc/nginx/sites-available/default 

sudo service nginx restart
