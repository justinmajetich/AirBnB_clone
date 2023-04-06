#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static?releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '\\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
