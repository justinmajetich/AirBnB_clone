#!/usr/bin/env bash
# Write a Bash script that sets up your web servers
#   for the deployment of web_static

# install nginx
sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install nginx
sudo service nginx start

# path creating
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# fake html file creating
sudo touch /data/web_static/releases/test/index.html
sudo echo "whatchamacallit" | sudo tee /data/web_static/releases/test/index.html

# symbolic link creating and ownership given to ubuntu user and group
ln -sfn /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data

# nginx config file editing
strToSearch="^\tlocation / {"
strToReplace="\tlocation /hbnb_static/ \
{ \n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"
sudo sed -i "s@${strToSearch}@${strToReplace}@" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
