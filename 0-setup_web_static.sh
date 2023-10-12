#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
    sudo apt-get -y update
    sudo apt-get -y install nginx


# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX Africa/Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group (recursively)
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve content
config_file="/etc/nginx/sites-available/default"
nginx_config="
location /hbnb_static {
    alias /data/web_static/current/;
}
"
sudo sed -i "/server_name _;/a $nginx_config" $config_file

# Restart Nginx service to apply the configuration changes
sudo service nginx restart
