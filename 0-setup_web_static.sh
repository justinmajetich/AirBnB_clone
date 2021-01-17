#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# Install NGINX
sudo apt-get -y update
sudo apt-get -y install nginx

# Create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML file
touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tDHK School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ownership of /data/ folder to user and group
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve content
content="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "37i\ $content" /etc/nginx/sites-enabled/default
sudo service nginx reload
sudo service nginx restart
