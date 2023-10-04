#!/usr/bin/env bash

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "This is a test." > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the appropriate user and group
chown -R  magnificent.tech:magnificent.tech /data/

# Update Nginx configuration

nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name magnificent.tech;

    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}"

# Save the Nginx configuration to a temporary file
echo "$nginx_config" > /tmp/nginx_config

# Replace the Nginx default configuration file
mv /tmp/nginx_config /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
