#!/usr/bin/env bash
# Prepares web servers for deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo -e "
<html>
\t<head>
\t</head>
\t<body>
\t\tHolberton School
\t</body>
</html>
" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
#sudo chown -R ubuntu /user/
#sudo chgrp -R ubuntu /user/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo service nginx restart
