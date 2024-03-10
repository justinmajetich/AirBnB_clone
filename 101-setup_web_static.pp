# 101-setup_web_static.pp
# This Puppet manifest configures a web server for the deployment of web_static.

# Define the Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By ${hostname};

    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=3MbaGJN2ioQ;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
                index index.html index.htm;
        }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
}"

# Ensure Nginx is installed
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

# Ensure the required directories exist
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure  => 'directory',
  require => Package['nginx'],
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Alx\n",
  require => File['/data/web_static/releases/test'],
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test/index.html'],
}

# Change ownership of the /data/ directory
exec { 'chown -R ubuntu:ubuntu /data/':
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  require => File['/data/web_static/current'],
}

# Ensure the /var/www/ and /var/www/html directories exist
file { ['/var/www', '/var/www/html']:
  ensure  => 'directory',
  require => Exec['chown -R ubuntu:ubuntu /data/'],
}

# Create the index.html and 404.html files
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School\n",
  require => File['/var/www/html'],
}

file { '/var/www/html/custom_404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
  require => File['/var/www/html'],
}

# Update the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
  require => File['/var/www/html/custom_404.html'],
}

# Restart Nginx
exec { 'nginx restart':
  path    => '/etc/init.d/',
  require => File['/etc/nginx/sites-available/default'],
}
