#!/usr/bin/env bash
# Sets up your web servers (web-01 & web-02) for the deployment of web_static

# colors
blue='\e[1;34m'
#brown='\e[0;33m'
green='\e[1;32m'
reset='\033[0m'

echo -e "${blue}Updating and doing some minor checks...${reset}\n"

# install nginx if not present
if [ ! -x /usr/sbin/nginx ]; then
        sudo apt-get update -y && \
                sudo apt-get upgrade -y && \
                        sudo apt-get install nginx -y
fi

echo -e "\n${blue}Setting up some minor stuff.${reset}\n"

# create directories
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# create index.html for test directory
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -fs /data/web_static/releases/test /data/web_static/current

# Give the user ownership of the dir
sudo chown -R ubuntu:ubuntu /data

# Set-up the content of /data/web_static/current/ to redirect to domain.tech/hbnb_static
sudo sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default

# Restart the nginx service to enforce the changes
sudo service nginx restart

echo -e "${green}Completed${reset}"
