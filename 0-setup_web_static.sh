#!/usr/bin/env bash
#
# Set up web servers for the deployment of web_static

apt update
apt -y install nginx

ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/shared /data/web_static/releases/test

cat > /data/web_static/releases/test/index.html << 'EOF'
<html>
  <head>
  </head>
  <body>
    Hello World
  </body>
</html>
EOF

ln -fns /data/web_static/releases/test /data/web_static/current

chown -hR ubuntu:ubuntu /data

sed -i '/^\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

service nginx restart
