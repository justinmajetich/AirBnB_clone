# using puppet to install and configure a web server

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
        return 301 http://linktr.ee/firdaus_h_salim/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# install nginx if not already installed
package {'nginx':
         ensure => 'installed',  
         provider => 'apt',
         }

# start nginx if not already running
service {'nginx':
         ensure => 'running',
         enable => true,
         }

# create folder /data/web_static
file {'/data/web_static':
      ensure => 'directory',
      }
# create folder /data/web_static/releases
file {'/data/web_static/releases':
      ensure => 'directory',
      }
# create folder /data/web_static/releases/test
file {'/data/web_static/releases/test':
      ensure => 'directory',
      }
# create folder /data/web_static/shared
file {'/data/web_static/shared':
      ensure => 'directory',
      }
# create folder /data/web_static/shared/test
file {'/data/web_static/shared/test':
      ensure => 'directory',
      }
# create file /data/web_static/releases/test/index.html
file {'/data/web_static/releases/test/index.html':
      ensure => 'file',
      content => '<html>
                  <head>
                  </head>
                  <body>
                    Holberton School
                  </body>
                  </html>',
      }
# create symbolic link /data/web_static/current
file {'/data/web_static/current':
      ensure => 'link',
      target => '/data/web_static/releases/test',
      }
# give ownership of /data/ to www-data
file {'/data/':
      ensure => 'directory',
      owner => 'ubuntu',
      group => 'ubuntu',
      mode => '0755',
      }
# add nginx config
# file {'/etc/nginx/sites-available/default':
#       ensure => 'file',
#       content => template('web_static/'),
#       notify => Service['nginx'],
#       }
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}
# restart nginx
exec { 'restart nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  require => File['/etc/nginx/sites-available/default'],
}