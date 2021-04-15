#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
if [ ! -d /data/ ]; then
  mkdir -p /data/web_static/shared/;
fi

if [ ! -d /data/ ]; then
  mkdir -p /data/web_static/releases/test/;
fi

echo -e '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}' etc/nginx/sites-available/default

service nginx restart
