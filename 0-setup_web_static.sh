#!/usr/bin/env bash
# A Bash script that sets up my web servers for the deployment of web_static

# Install Nginx if not already installed
if [ "$(dpkg-query -l nginx | wc -l)" -le 1 ]; then
    apt -y update
    apt install -y nginx
fi

# Create the folders:
#+ /data/ 
#+ /data/web_static/
#+ /data/web_static/releases/
#+ /data/web_static/releases/test/
#+ /data/web_static/shared/     
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

echo "$TEMP" > /data/web_static/releases/test/index.html

# Create symlink current for releases/test/ directory
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership of data folder to ubuntu
chown -R ubuntu:ubuntu /data/

CONFIG_FILE="/etc/nginx/sites-enabled/default"
CONFIG_TEMP="\tserver_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "s~^\tserver_name _;~$CONFIG_TEMP~g" "$CONFIG_FILE"

# restart nginx service
service nginx restart
