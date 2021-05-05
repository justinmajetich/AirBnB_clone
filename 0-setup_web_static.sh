#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
IsNginx=$(which nginx)
if [ -z "$IsNginx" ]; then
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get -y install nginx
fi
sudo ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html>
  <head>
  </head>
  <body>
    ¡Vamo La Cooperativa!
  </body>
</html>" > /data/web_static/releases/test/index.html
if [ -e "/data/web_static/current" ]; then
    rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
new_string="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"
sed -i "42i $new_string" /etc/nginx/sites-available/default
sudo service nginx restart
