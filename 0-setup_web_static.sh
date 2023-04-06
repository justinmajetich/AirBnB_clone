#!/usr/bin/env bash
# Check if Nginx is installed
if ! command -v nginx &> /dev/null
then
    # Install Nginx if it is not installed
    echo "Nginx is not installed. Installing..."
    sudo apt-get -y update
    sudo apt-get -y install nginx
    echo "Nginx has been installed."
else
    # Print a message if Nginx is already installed
    echo "Nginx is already installed."
fi

# starting nginx service
sudo service nginx start
sudo ufw allow 'Nginx HTTP'

#Create the dirs
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "The Dir's are created"

#Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
cat <<EOF > "/data/web_static/releases/test/index.html"
        <h1>NGS's Test Page</h1>
        <p>This page is created to test the Nginx configuration.</p>
EOF

echo "HTML file has been created at /data/web_static/releases/test/index.html"

# Create the new symbolic link and change ownership
if [ -L "$/data/web_static/current" ]; then
    sudo rm "/data/web_static/releases/test/"
fi
sudo ln -s "/data/web_static/current" "/data/web_static/releases/test/"

echo "Symbolic link has been created at /data/web_static/releases/test/"
sudo chown -R "ubuntu:ubuntu" "/data/"

#configure Nginx
echo "alias /hbnb_static $source_path;" | sudo tee /etc/nginx/sites-available/default > /dev/null
# Restart Nginx
sudo service nginx restart
echo "Nginx configuration has been updated to serve $source_path to /hbnb_static"
