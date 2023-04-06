# Setup the web servers for the deployment of web_static
exec { '/usr/bin/env apt -y update' : }
-> package { 'nginx':
  ensure => installed,
}
-> file { '/data':
  ensure  => 'directory'
}
-> file { '/data/web_static':
  ensure => 'directory'
}
-> file { '/data/web_static/releases':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}
-> file { '/data/web_static/shared':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>"
}
-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}
-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
-> file { '/var/www':
  ensure => 'directory'
}
-> file { '/var/www/html':
  ensure => 'directory'
}
-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>"
}
exec { 'nginx_conf':
  environment => ['data=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sed -i "39i $data" /etc/nginx/sites-enabled/default',
  path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
}
-> service { 'nginx':
  ensure => running,
}
