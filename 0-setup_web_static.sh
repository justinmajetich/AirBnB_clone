et up web servers for deployment of web_static
apt update
apt install nginx -y
mkdir -p /data/web_static/releases/test
mkdir /data/web_static/shared
echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School is driving me into the ground\n</body>\n</html>\n" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

sed -i "s|error_page 404 /404.html;|error_page 404 /404.html;\n\nlocation /hbnb_static {\n\talias /data/web_static/current/;\n}|" /etc/nginx/sites-available/default

service nginx restart
