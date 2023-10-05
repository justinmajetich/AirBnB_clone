#!/usr/bin/env bash
# setting up the webserver for static deployment

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
echo "testing" > /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/server_name/a \ \n\t location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t }" /etc/nginx/sites-available/default
state=$(pgrep nginx)
if [ -n "$state" ];
then
        sudo service nginx restart
else
        sudo service nginx start
fi
echo "done!!!"

