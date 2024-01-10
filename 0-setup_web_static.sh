#!/usr/bin/env bash
#Script that sets up your web servers for the deployment of web_static

if ! dpkg -s nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

html="<html>
<head></head>
<body>
  Holberton School
</body>
</html>"

echo "$html" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"

if ! grep -q "location /hbnb_static {" "$nginx_config"; then
    sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"
fi

sudo service nginx restart
