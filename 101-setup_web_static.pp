# Task 2
# comment

$indx = "<html>
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>
"

$s = "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        location /hbnb_static {
                alias /data/web_static/current/;
        }
        rewrite '^/redirect_me$' http://example.com permanent;
        add_header X-Served-By ${hostname};
        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /var/www/html;
                internal;
        }
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
}"

exec {'apt-update':
  command => '/usr/bin/env apt-get -y update',
}

-> file {['/data', '/data/web_static', '/data/web_static/shared',
          '/data/web_static/releases', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

-> package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

-> file {'/data/web_static/releases/test/index.html':
  ensure  => 'file',
  path    => '/data/web_static/releases/test/index.html',
  content => "${indx} ",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

-> file {['/var', '/var/www/ebukaejie', '/var/www/ebukaejie/html']:
  ensure => 'directory',
}

-> file {'/var/www/ebukaejie/html/index.html':
  ensure  => 'file',
  path    => '/var/www/ebukaejie/html/index.html',
  content => "Hello World!",
}

-> file {'custom_404.html':
  ensure  => 'file',
  path    => '/var/www/ebukaejie/html/custom_404.html',
  content => "Ceci n'est pas une page",
}


-> file {'/etc/nginx/sites-available/default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  content => "${s} ",
}

-> file {'/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

-> exec {'chown':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}

-> service {'nginx':
  ensure  => 'running',
  restart => 'sudo service nginx restart',
}
