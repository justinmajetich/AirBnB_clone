#!/usr/bin/env bash
#set things up for deployment

if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update -y -qq && \
	    sudo apt-get install -y nginx
fi


# make dirs...
sudo mkdir -p /data/web_static/releases/test  /data/web_static/shared/


echo "<h1> I couldn't center a div </h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# create sym link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/


sudo cp /etc/nginx/sites-enabled/default /etc/nginx/nginx-sites-enabled_default.bck


sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
