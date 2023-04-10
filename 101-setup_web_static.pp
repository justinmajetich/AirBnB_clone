# Puppet script that sets up your web servers
# for the deployment of web_static.

# update software packages list
exec { 'update packages':
  command => 'sudo apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx
package { 'nginx':
  ensure     => 'installed',
}

# Create the test folder recurlsively if not exist.
exec { '/data/web_static/releases/test':
  command => 'sudo mkdir -p /data/web_static/releases/test',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Create shared folder
exec { '/data/web_static/shared/':
  command => 'sudo mkdir -p /data/web_static/shared/',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# create index file
$index_content = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $index_content,
}

# Create a symbolic link called 'current' to test folder.
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Give ownership of the /data/ folder to the ubuntu user AND group
exec { 'chown /data/ folder':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { '/var/www/html':
  ensure => 'directory'
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!\n"
}

# Nginx configurations Update
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'present',
  content =>
"
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                add_header X-Served-By $(hostname);
                try_files \$uri \$uri/ =404;
        }
        location /hbnb_static/ {
                alias /data/web_static/current/;
                add_header X-Served-By $(hostname);
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }

        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page - Error page\n"
}

# restart nginx
exec { 'restart service':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start service nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
