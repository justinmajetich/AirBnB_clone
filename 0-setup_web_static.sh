#!/usr/bin/env bash
# bash script to setup web server for hosting web_static

# colors
blue='\e[1;34m'
green='\e[1;32m'
reset='\033[0m'

echo -e "\n\t${blue}Installing nginx if it's not installed${reset}\n"
command -v nginx
if [ $? -eq 1 ]; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

echo -e "\n\t${blue}Creating the folders if they don't exist${reset}\n"
if [ ! -d /data/web_static/releases/test/ ]; then
	sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
fi
sudo mkdir -p /var/www/html /var/www/error
sudo chmod -R 755 /var/www
echo "Hello World!" | sudo tee /var/www/html/index.html
echo "Ceci n'est pas une page" | sudo tee /var/www/error/404.html

echo -e "\n\t${blue}Creating a fake HTML file${reset}\n"
FILE="<!DOCTYPE html>
<html lang=\"en\">
	<head>
		<meta charset=\"UTF-8\">
		<title>AirBnB clone - Web static</title>
	</head>
	<body>
		<h1>AirBnB clone - Web static</h1>
	</body>
</html>"
echo "$FILE" | sudo tee /data/web_static/releases/test/index.html

echo -e "\n\t${blue}Creating a symbolic link${reset}\n"
if [ -h /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

echo -e "\n\t${blue}Giving ownership of the /data/ folder to the ubuntu user and group${reset}\n"
sudo chown -R ubuntu:ubuntu /data/

echo -e "\n\t${blue}Updating the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static${reset}\n"
CONFIG="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/error/;
        internal;
    }

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
"
echo "$CONFIG" | sudo tee /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

echo -e "\n\t${blue}Restarting nginx${reset}\n"
sudo service nginx restart

echo -e "\n\t${green}Done!${reset}\n"
