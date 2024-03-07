# == Class: web_static_setup
#
# This class sets up web servers for the deployment of web_static.
#
class web_static_setup {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the required directories exist
  file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Ensure the fake HTML file exists
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'present',
    content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  # Ensure the symbolic link exists
  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    force  => true,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
  file_line { 'nginx_config':
    path  => '/etc/nginx/sites-available/default',
    line  => '    location /hbnb_static { alias /data/web_static/current/; }',
    match => '^    location /hbnb_static',
    after => 'server_name _;',
  }

  # Ensure Nginx is running
  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

include web_static_setup
