#!/usr/bin/env bash
# using fabric to deploy airbnb web static

# update packages list
sudo apt-get update

#install nginx if not installed
if ! command -v nginx &> /dev/null
then
  sudo apt-get install nginx -y
fi
sudo ufw allow 'Nginx HTTP'

#create a folder /data/ if it doesn't exist
# the -p helps prevent errors if the directory/subdirectories exists
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create a fake html file
echo "<html>
      <head>
      </head>
      <body>
        Holberton School
      </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link ..current linked to ..test/ folder
# if the link exists, should be deleted and recreated
sudo ln -sf /data/web_static/releases/test/  /data/web_static/current

# give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx configuration to serve content of (/data/web_static/current/) to (hbnb_static)
sudo sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart