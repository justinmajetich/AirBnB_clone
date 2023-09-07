class web_server_setup {

  # Update APT packages
  exec { 'update':
    command => '/usr/bin/apt-get update',
  }

  # Install Nginx package
  package { 'nginx':
    ensure   => 'present',
    provider => 'apt',
  }

  # Create directory structure with defined types
  web_directory { '/data/': }
  web_directory { '/data/web_static/': }
  web_directory { '/data/web_static/releases/': }
  web_directory { '/data/web_static/shared/': }
  web_directory { '/data/web_static/releases/test/': }

  # Create HTML index page
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'present',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => "Holberton School Puppet\n",
  }

  # Create symbolic link
  file { '/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    force   => true,
  }

  # Change ownership
  exec { 'chown':
    command => 'chown -R ubuntu:ubuntu /data/',
    path    => '/usr/bin/:/usr/local/bin/:/bin/',
    refreshonly => true,
  }

  # Update Nginx configuration
  exec { 'sed':
    command => "sed -i '/^\\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    require => Package['nginx'],
  }

  # Restart Nginx
  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Exec['sed'],
  }
}

define web_directory($path) {
  file { $path:
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    require => Package['nginx'],
  }
}

include web_server_setup