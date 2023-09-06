#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static. It must:

# Update & Install nginx
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y nginx

# create files
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# create HTML index page
echo "MA-Abahmane" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link /data/web_static/current linked
# to the /data/web_static/releases/test/ folder
# If the symbolic link already exists, it should be deleted
# and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R -h ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# EX: https://mydomainname.tech/hbnb_static
location='\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'
sudo sed -i '40i\'"$location" /etc/nginx/sites-available/default


# Reload Nginx to load changes
sudo service nginx reload
