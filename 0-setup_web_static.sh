#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# Update package lists
apt update

# Install Nginx
apt install -y nginx

# - Create the folders, if they don't yet exist:
#   * '/data'
#   * '/data/web_static/'
#   * '/data/web_static/releases/'
#   * '/data/web_static/releases/test/'
#   * '/data/web_static/shared/'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file '/data/web_static/releases/test/index.html',
# (with simple content, to test Nginx configuration)
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" | 
tee /data/web_static/releases/test/index.html 

# Create a symbolic link '/data/web_static/current' linked to the
# '/data/web_static/releases/test/' folder.
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give recursive ownership of the '/data/' folder to the 'ubuntu' user AND group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of '/data/web_static/current/'
# to 'hbnb_static' (ex: https://mydomainname.tech/hbnb_static).
loc_header="location \/hbnb\_static\/ {"
loc_content="alias \/data\/web\_static\/current\/;"
new_location="\n\t$loc_header\n\t\t$loc_content\n\t}\n"
sed -i "37s/$/$new_location/" /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
