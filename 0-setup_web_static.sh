#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
    sudo apt-get -y update
    sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create HTML file
echo "<html>
  <head>
  </head>
  <body>
    ALX Africa/Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
nginx_config="location /hbnb_static/ {\\n    alias /data/web_static/current/;\\n}"
sudo sed -i "/server_name _;/a $nginx_config" $config_file

# Restart the Nginx service to apply the configuration changes
sudo service nginx restart
