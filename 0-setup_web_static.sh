#!/usr/bin/env bash
# Prepare your web servers
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown -R ubuntu:ubuntu /data/
new_redirect="server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i 's|server_name _;|'"$new_redirect"'|' /etc/nginx/sites-enabled/default
sudo service nginx restart
