#!/usr/bin/env bash
# This script sets up web servers for web_static deployment

# Install Nginx if not already installed
if ! [ "$(command -v nginx)" ]; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary folders with proper ownership
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
chown -R ubuntu:ubuntu /data

# Create a test HTML file
echo "<html>
	<head>
	</head>
	<body>
	  Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html

# Manage symbolic link for current release
rm -rf /data/web_static/current || true
ln -s /data/web_static/releases/test /data/web_static/current

# Update Nginx configuration
cat << EOF > /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $HOSTNAME;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
        try_files \$uri \$uri/  =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=3MbaGJN2ioQ;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
}
EOF

# Reload Nginx configuration
nginx -t > /dev/null 2>&1 && service nginx reload
