#!/usr/bin/env bash
# install nginx if not installed

if ! which nginx;
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# create folders if they don't exist
if [[ ! -e /data/web_static/releases/test/ ]];
then
    sudo mkdir -p /data/web_static/releases/test/
fi

if [[ ! -e /data/web_static/shared/ ]];
then
    sudo mkdir -p /data/web_static/shared/
fi

# create dummy html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" > /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# chown of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx confi to serve content of /data/web_static/current to hbnb_static
sudo sed -i '39i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart
