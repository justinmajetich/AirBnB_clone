#!/usr/bin/env bash
# this script sets up a webserver for deployment of dir "web_static"

# install nginx
apt-get update -y
apt-get install -y nginx

# create directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# create test index file
echo "
<html>
<head>
  <title>Test page</title>
</head>
<body>
  <p> Everything works! </p>
</body>
</html>
" >  /data/web_static/releases/test/index.html

# create a symlink
ln -sfn /data/web_static/releases/test/ /data/web_static/current

# give ownership of "data" dir to  user "ubuntu"
chown -R ubuntu:ubuntu /data/

# update nginx config to serve content of
# /data/web_static/current/ to hbnb_static
config_file="/etc/nginx/sites-available/default"
config_line="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
# add the config line if doesn't already exist in the file
if ! grep -q "location /hbnb_static/" "$config_file"; then
  sed -i "/listen 80 default_server;/a $config_line" "$config_file"
fi

# restart nginx
service nginx restart
