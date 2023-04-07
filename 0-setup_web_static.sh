#!/usr/bin/env bash
# This script sets up an Nginx server for Static Web Deployment.

# shellcheck disable=SC2154

# Install nginx engine if not exist.
NGX_STATUS=$(dpkg -s nginx 2>/dev/null | grep -c "ok installed")

if [ "$NGX_STATUS" -eq 0 ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create the test folder recurlsively if not exist.
TEST_FOLDER='/data/web_static/releases/test'
sudo mkdir -p $TEST_FOLDER
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file (index.html) inside of test folder.
FILE_CONTENT=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

PATH_TO_INDEX="$TEST_FOLDER"/index.html
echo -e "$FILE_CONTENT" > $PATH_TO_INDEX

# Create a symbolic link called 'current' to test folder.
sudo ln -sf $TEST_FOLDER /data/web_static/current 

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Nginx configurations Update
HOST_NAME=$(hostname)
NGX_CONFIG=\
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;

	location / {
                add_header X-Served-By $HOST_NAME
		try_files \$uri \$uri/ =404;
	}

        location /hbnb_static/ {
                alias /data/web_static/current/;
                add_header X-Served-By $HOST_NAME
        }

        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
"
echo "Ceci n'est pas une page" > /var/www/html/404.html
echo "$NGX_CONFIG" > /etc/nginx/sites-available/default

if [ "$(pgrep -c nginx)" -le 0 ];
then
    service nginx start
else
    service nginx restart
fi;
