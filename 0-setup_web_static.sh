#!/usr/bin/env bash
<<<<<<< HEAD
# Bash script that sets up web servers for the development of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Ngnix HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/release/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/release/test/
sudo touch /data/web_static/release/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
   Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static {alis /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart 
=======
# Install Nginx if it's not already installed
if ! command -v nginx &> /dev/null
then
    echo "Nginx is not installed. Installing..."
    sudo apt-get update && sudo apt-get -y install nginx
fi

# Create required directories if they don't exist
directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for folder in "${directories[@]}"
do
    if [ ! -d "$folder" ]; then
        sudo mkdir -p "$folder"
        echo "Folder $folder has been created."
    else
        echo "Folder $folder already exists."
    fi
done

# Create fake HTML file for testing Nginx configuration
sudo echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
echo "Fake HTML file created at /data/web_static/releases/test/index.html"

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
echo "Symbolic link created at /data/web_static/current"

# Change ownership of /data/ folder to ubuntu user
sudo chown -R ubuntu:ubuntu /data/
echo "Ownership of /data/ folder has been changed to ubuntu:ubuntu"

# Update Nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
echo "Nginx configuration updated and service restarted."
>>>>>>> b1103445917867caa901a652db20496d0a667344
