#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y  install nginx
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html && echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
current_link="/data/web_static/current"
target_folder="/data/web_static/releases/test/"
if [ -L "$current_link" ]; then
    sudo rm "$current_link"
fi
sudo ln -s "$target_folder" "$current_link"
sudo chown -R ubuntu:ubuntu /data/
# sed -i '14i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo sed -i '/server {/a\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx start
