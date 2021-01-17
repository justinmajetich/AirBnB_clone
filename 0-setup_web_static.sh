#!/usr/bin/env bash
<<<<<<< HEAD
# Sets up the web servers for the deployment of web_static

# Install NGINX
sudo apt-get -y update
sudo apt-get -y install nginx

# Create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML file
touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tDHK School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ownership of /data/ folder to user and group
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve content
content="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "37i\ $content" /etc/nginx/sites-enabled/default
sudo service nginx reload
sudo service nginx restart
=======
#web servers for the deployment 
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Test Code
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0
>>>>>>> 76c50d006b6549abb644e7e6a4e1f8f89ef3866e
