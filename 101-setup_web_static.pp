# Sets up web servers for the deployment of web_static using Puppet

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://github.com/lebogangolifant/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# Install Nginx
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->

# Create necessary directories
file { '/data':
  ensure  => 'directory',
} ->

file { '/data/web_static':
  ensure => 'directory',
} ->

file { '/data/web_static/releases':
  ensure => 'directory',
} ->

file { '/data/web_static/shared':
  ensure => 'directory',
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory',
} ->
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "ALX Africa/Holberton School Puppet\n",
} ->
