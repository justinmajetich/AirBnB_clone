#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chmod 777 /data/web_static/releases/test/
sudo echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/pass the PHP/i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
