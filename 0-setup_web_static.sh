#!/usr/bin/env bash
<<<<<<< HEAD
# Bash script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# creating the directories of the following if not  there alredy
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# Create a fake HTML file '/data/web_static/releases/test/index.html',
# (with simple content, to test Nginx configuration)
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link '/data/web_static/current' linked to 
# the '/data/web_static/releases/test/' folder
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give recursive ownership of the '/data/' folder to the 'ubuntu' user AND group
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart Nginx
sudo service nginx restart

=======
# script that sets up your web servers for the deployment of web_static
server="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
echo "Holberton" >"/data/web_static/releases/test/index.html"
rm -f "/data/web_static/current"
ln -s "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -hR ubuntu:ubuntu "/data/"
sudo sed -i "29i\ $server" "$file"
sudo service nginx restart
>>>>>>> f38d68f0b60b9b15746a7c75357b2fef7e45506c
