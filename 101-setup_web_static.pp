#  Redo the task #0 but by using Puppet:

exec { 'custom http header':
command  => "
sudo apt-get update;
sudo apt-get upgrade -y;
sudo apt-get install -y nginx;

sudo mkdir -p /data/web_static/shared;
sudo mkdir -p /data/web_static/releases/test;

echo 'MA-Abahmane' | sudo tee /data/web_static/releases/test/index.html;

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;

sudo chown -R -h ubuntu:ubuntu /data/;

location='location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n';
sudo sed -i '40i\\t''$location' /etc/nginx/sites-available/default;

sudo service nginx restart;",
provider => shell,
}
