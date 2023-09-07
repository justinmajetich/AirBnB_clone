# Define a Puppet class to configure the web server
class web_server_setup {

  package { 'nginx':
    ensure => 'installed',
  }

  file { '/data/web_static/shared':
    ensure  => 'directory',
    recurse => true,
  }

  file { '/data/web_static/releases/test':
    ensure  => 'directory',
    recurse => true,
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => 'MA-Abahmane',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    force  => true,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  exec { 'change_ownership':
    command     => 'chown -R ubuntu:ubuntu /data/',
    refreshonly => true,
  }

  file { '/etc/nginx/sites-available/default':
    content => template('web_server_setup/nginx_config.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}
