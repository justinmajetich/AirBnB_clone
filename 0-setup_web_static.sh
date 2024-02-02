#!/usr/bin/env bash
# Setup web servers for the deployment of web_static

echo "Updating apt package list and installing nginx"
apt -qq update && apt install -y nginx

if [ ! -d "/data/" ]; then
    echo "Creating /data/ folder"
    mkdir -p /data/
fi

if [ ! -d "/data/web_static/" ]; then
    echo "Creating /data/web_static/ folder"
    mkdir -p /data/web_static/
fi

if [ ! -d "/data/web_static/releases/" ]; then
    echo "Creating /data/web_static/releases/"
    mkdir -p /data/web_static/releases/
fi

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir -p /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    echo "Creating /data/web_static/releases/test/ folder"
    mkdir -p /data/web_static/releases/test/
fi

if [ ! -f "/data/web_static/releases/test/index.html" ]; then
    echo "Creating index.html in /data/web_static/releases/test/ folder"
    touch /data/web_static/releases/test/index.html
fi

echo "Writing content to index.html"
cat > /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

if [ ! -d "/data/web_static/current" ]; then
    echo "Creating symlink for /data/web_static/releases/test/"
    ln -sfn /data/web_static/releases/test/ /data/web_static/current
fi

echo "Give right to user and group ubuntu to /data"
chown -R ubuntu:ubuntu /data/

echo "Writing to nginx configuration file"
cat > /etc/nginx/sites-enabled/default <<"EOF"
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files $uri $uri/ =404;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404.html;

	location /hbnb_static {
		 alias /data/web_static/current/;
	}
}
EOF

echo "Restarting nginx server"
service nginx restart
