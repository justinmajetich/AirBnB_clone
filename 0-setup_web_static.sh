#!/usr/bin/python3
# sets up web server for the deployment of web static

#install Nginx
sudo apt-get update
sudo apt-install -y nginx

#create the folders
mkdir -p /data/
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
touch -p /data/web_static/releases/test/index.html

echo "
<html>
<head>
</head>
<body>
	ALX Holberton School
</body>
</html>
" > /data/web_static/releases/test/index.html

sudo service nginx restart
