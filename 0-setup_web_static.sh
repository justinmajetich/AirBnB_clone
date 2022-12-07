#!/usr/bin/env bash
# Installs, configures, and starts the web server
SERVER_CONFIG="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        add_header X-Served-By \$hostname;
        location / {
                try_files \$uri \$uri/ =404;
                error_page 404 /404.html;
        }
        location /redirect_me{
                return 301 https://github.com/felixobianozie;
        }
        location /rewrite_me{
                rewrite / /rewrite.html;
        }
        location /404.html{
                root /var/www/error;
                index 404.html;
        }
	location /hbnb_static/ {
                alias /data/web_static/current/;
                try_files \$uri \$uri/ =404;
	}
}"
HOME_PAGE="<!DOCTYPE html>
<html lang='en-US'>
	<head>
		<title>Home - AirBnB Clone</title>
	</head>
	<body>
		<h1>Welcome to AirBnB!</h1>
	<body>
</html>
"
# shellcheck disable=SC2230
# Check that nginx exists, else install it
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
    apt-get update
    apt-get -y install nginx
fi

# Persist previous configuration
mkdir -p /var/www/error
touch /var/www/error/404.html
touch /var/www/html/rewrite.html
echo "Your rewrite request has been implemented!" > /var/www/html/rewrite.html
echo "Ceci n'est pas une page" > /var/www/error/404.html

# Updated configuration
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "$HOME_PAGE" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-available/default"
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
fi