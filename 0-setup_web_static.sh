#!/usr/bin/env bash
<<<<<<< HEAD
# To set-up the web server for deploying of Airbnb web static page
# Creates folders where static pages will be stored
# creates symbolic link
apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>

" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current


chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://github.com/rodgersxy;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
=======
# A Bash script that sets up your web servers for the deployment of web_static. It must:

# Update & Install nginx
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y nginx

# create files
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# create HTML index page
echo "MA-Abahmane" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link /data/web_static/current linked
# to the /data/web_static/releases/test/ folder
# If the symbolic link already exists, it should be deleted
# and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R -h ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# EX: https://mydomainname.tech/hbnb_static
location='location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n'
sudo sed -i '40i\\t'"$location" /etc/nginx/sites-available/default

# Reload Nginx to load changes
sudo service nginx restart
>>>>>>> 3e6a2afc434e5bb107bd4fca095634e29067244d
