#!/usr/bin/python3
# Puppet script to configure a web server for deployment of web_static

# Install Nginx
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
} ->

# Ensure necessary directories and permissions
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
} ->

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "
    server {
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
            return 301 http://cuberule.com/;
        }

        error_page 404 /404.html;
        location /404 {
          root /var/www/html;
          internal;
        }
    }
  ",
} ->

# Restart Nginx
exec { 'nginx_restart':
  command => '/usr/sbin/service nginx restart',
}

