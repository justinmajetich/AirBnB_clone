# web_server_setup.pp
# Description: Puppet manifest to set up a web server for deployment of web_static.

# Updates the server packages
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

# Installs Nginx package if not installed
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

# Creates necessary directories
file { '/data/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true, # Ensures recursive ownership
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    H
