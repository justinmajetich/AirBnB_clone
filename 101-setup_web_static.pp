# Configures a web server for deployment of web_static.
# Nginx configuration file

$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm 103-index.html;
    }
    location /redirect_me {
        return 301 https://github.com/Trefania;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}
file { '/data':
  ensure => 'directory',
  owner  => "ubuntu",
  group  => "ubuntu"
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => "ubuntu",
  group  => "ubuntu"
}
file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => "ubuntu",
  group  => "ubuntu"
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => "ubuntu",
  group  => "ubuntu"
}
file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => "ubuntu",
  group  => "ubuntu"
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  owner   => "ubuntu",
  group   => "ubuntu",
  content => "Holberton School\n"
}

file { '/data/web_static/current':
  ensure => 'link',
  owner  => "ubuntu",
  group  => "ubuntu",
  target => '/data/web_static/releases/test'
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}
file { '/var/www/html':
  ensure => 'directory'
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School\n"
}
file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}
