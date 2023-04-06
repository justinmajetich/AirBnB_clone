#!/usr/bin/env bash
#Set up my server for deployment
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

#Create the direrctories
folder="/data/web_static/shared"

# Check if the folder exists
if [ ! -d "$folder" ]; then
    # Create the folder if it does not exist
    echo "Folder does not exist. Creating folder..."
    sudo mkdir -p "$folder"
    echo "Folder has been created."
else
    # Print a message if the folder already exists
    echo "Folder already exists."
fi

folder="/data/web_static/releases/test"

# Check if the folder exists
if [ ! -d "$folder" ]; then
    # Create the folder if it does not exist
    echo "Folder does not exist. Creating folder..."
    sudo mkdir -p "$folder"
    echo "Folder has been created."
else
    # Print a message if the folder already exists
    echo "Folder already exists."
fi

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
sudo ln -s "/data/web_static/current" "/data/web_static/releases/test"

echo "Symbolic link has been created at /data/web_static/releases/test"
sudo chown -R "ubuntu:ubuntu" "/data"

#configure Nginx
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart Nginx
sudo service nginx restart
echo "Nginx configuration has been updated to serve $source_path to /hbnb_static"
