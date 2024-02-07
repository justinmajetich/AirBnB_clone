#!/usr/bin/env bash
## Bash scrip to set up web servers to deploy web_static
sudo apt-get update
sudo apt-get install nginx
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" |sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
