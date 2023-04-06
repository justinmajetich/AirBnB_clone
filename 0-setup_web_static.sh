#!/usr/bin/env bash
#Set up my server for deployment
if ! command -v nginx &> /dev/null
then
    #--Install Nginx if it is not installed
    echo "Nginx is not installed. Installing..."
    sudo apt-get -y update
    sudo apt-get -y install nginx
    echo "Nginx has been installed."
else
    #--Print a message if Nginx is already installed
    echo "Nginx is already installed."
fi
echo

#--starting nginx service
sudo service nginx start
sudo ufw allow 'Nginx HTTP'
echo
#--Create the directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo

echo "The Dir's are created"

if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;
echo

#Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo "<h1>NGS's Test Page</h1>  <p>This page is created to test the Nginx configuration.</p>" > /data/web_static/releases/test/index.html
echo "HTML file has been created at /data/web_static/releases/test/index.html"
echo
# Create the new symbolic link
if [ -L "/data/web_static/current" ]; then
  sudo  rm /data/web_static/current
  echo "Removed existing symlink: /data/web_static/current"
fi
echo
ln -s /data/web_static/releases/test /data/web_static/current
echo "Created new symlink: /data/web_static/current -> /data/web_static/releases/test"
sudo chown -hR ubuntu:ubuntu /data
echo
#configure Nginx
echo "alias /hbnb_static /data/web_static/current" | sudo tee /etc/nginx/sites-available/default > /dev/null
# Restart Nginx
sudo service nginx restart
echo "Nginx configuration has been updated to serve $source_path to /hbnb_static"
echo

