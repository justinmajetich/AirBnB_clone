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
echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

# Manage symbolic link for current release
rm -rf /data/web_static/current || true
ln -s /data/web_static/releases/test /data/web_static/current

# Update Nginx configuration for hbnb_static
cat << EOF > /etc/nginx/sites-available/hbnb_static
server {
    listen 80;
    server_name eduresource.tech;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF
ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/

# Reload Nginx configuration
nginx -t && service nginx reload
