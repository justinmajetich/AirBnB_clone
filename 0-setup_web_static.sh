#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update && sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello Friends" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER":"$USER" /data
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
