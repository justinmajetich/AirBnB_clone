#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data

CONFIGURED=$(grep -c "location /hbnb_static/ {" /etc/nginx/sites-available/default)

if [ "$CONFIGURED" = 0 ]; then
    sed -i "/^\tserver_name/a \\\n\tlocation /hbnb_static/ {" /etc/nginx/sites-available/default
    sed -i "/^\tlocation \/hbnb_static/a \\\t}" /etc/nginx/sites-available/default
    sed -i "/^\tlocation \/hbnb_static/a \\\t\talias /data/web_static/current/;" /etc/nginx/sites-available/default
fi

service nginx restart
