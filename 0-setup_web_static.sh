#!/usr/bin/env bash
# A Bash script that sets up my web servers for the deployment of web_static

# Install Nginx if not already installed
apt -y update
apt install -y nginx

# Create the folders:
#+ /data/ 
#+ /data/web_static/
#+ /data/web_static/releases/
#+ /data/web_static/releases/test/
#+ /data/web_static/shared/     
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

HTML_TEMP=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$HTML_TEMP" > /data/web_static/releases/test/index.html

# Create symlink current for releases/test/ directory
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership of data folder to ubuntu
chown -R ubuntu:ubuntu /data/

sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

# restart nginx service
service nginx restart
