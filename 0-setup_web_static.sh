#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# Installing Nginx
apt-get update -y
apt-get upgrade -y
apt-get install nginx -y

# Creating folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Creating fake HTML file
echo '
<!DOCTYPE html>
<html>
<head>
<title>Fake HTML</title>
</head>
<body>
<h1>Fake HTML file</h1>
<p>Fake HTML file with basic content</p>
</body>
</html> ' > /data/web_static/releases/test/index.html

# Creating symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership to ubuntu user and group
chown -hR ubuntu:ubuntu /data/

# Updating Nginx configuration
sed -i '40i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restarting Nginx
service nginx restart
