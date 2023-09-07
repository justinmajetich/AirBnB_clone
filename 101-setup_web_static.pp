# Redo the task #0 but by using Puppet:

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data/':
    group  => 'ubuntu',
    owner  => 'ubuntu',
    ensure => 'directory',
} ->

file { '/data/web_static/':
    group  => 'ubuntu',
    owner  => 'ubuntu',
    ensure => 'directory',
} ->

file { '/data/web_static/releases/':
    owner  => 'ubuntu',
    group  => 'ubuntu',
    ensure => 'directory',
} ->

file { '/data/web_static/shared/':
    owner  => 'ubuntu',
    group  => 'ubuntu',
    ensure => 'directory',
} ->

file { '/data/web_static/releases/test/':
    owner  => 'ubuntu',
    group  => 'ubuntu',
    ensure => 'directory',
} ->

file { '/data/web_static/releases/test/index.html':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  ensure  => 'present',
  content => "Holberton School Puppet\n",
  path    => '/data/web_static/releases/test/index.html',
} ->

file { '/data/web_static/current':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  ensure  => 'link',
  replace => 'yes',
  target  => '/data/web_static/releases/test',
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

exec { 'sed':
  command => "sed -i \
  '/^\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
