#!/usr/bin/env bash
#Set up my server for deployment

#Install Nginx
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
#Allow a firewall
sudo ufw allow 'Nginx HTTP'


#Create the Directories
if [ ! -d "/data/web_static/releases/test" ]; then
  sudo mkdir -p /data/web_static/releases/test
fi

if [ ! -d "/data/web_static/shared" ]; then
  mkdir -p /data/web_static/shared
fi

#Create a fake HTML file to test Nginx
echo "<h1>NGS's Test Page</h1>  <p>This page is created to test the Nginx configuration.</p>" > /data/web_static/releases/test/index.html

#change owner and group
sudo chown -hR ubuntu:ubuntu /data


#create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#update Nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#restart NGINX
sudo service nginx restart

