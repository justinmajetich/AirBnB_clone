#!/usr/bin/env bash
# Install Nginx if it not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create the folder /data/ if it doesn’t already exist
if ! [ -d "/data/" ]; then
  sudo mkdir /data/
fi

# Create the folder /data/web_static/ if it doesn’t already exist
if ! [ -d "/data/web_static/" ]; then
  sudo mkdir /data/web_static/
fi

# Create the folder /data/web_static/releases/ if it doesn’t already exist
if ! [ -d "/data/web_static/releases/" ]; then
  sudo mkdir /data/web_static/releases/
fi

# Create the folder /data/web_static/shared/ if it doesn’t already exist
if ! [ -d "/data/web_static/shared/" ]; then
  sudo mkdir /data/web_static/shared/
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if ! [ -d "/data/web_static/releases/test/" ]; then
  sudo mkdir /data/web_static/releases/test/
fi

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
sudo sed -i 's/server_name _;/server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n/' /etc/nginx/sites-available/default
sudo service nginx restart
