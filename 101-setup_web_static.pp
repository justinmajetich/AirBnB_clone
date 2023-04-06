# Puppet manifest to set up a web server for deployment of web_static.

# Update package repositories
package { 'update':
  provider => 'apt',
  before   => Package['nginx'],
}
 
# Install Nginx web server
package { 'nginx':
  ensure  => 'installed',
  require => Package['update'],
}

# Create directory structure for web_static
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create index.html with content "Holberton School"
file { '/data/web_static/releases/test/index.html':
  content => "Holberton School\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link for /data/web_static/current to /data/web_static/releases/test/
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Configure Nginx web server
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $HOSTNAME;
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
    }",
  owner => 'root',
  group => 'root',
  mode  => '0644',
}

# Restart Nginx service
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
