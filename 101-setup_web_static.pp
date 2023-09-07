# Redo the task #0 but by using Puppet:

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/shared/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/test/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "Holberton School Puppet\n",
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  replace => 'yes',
  owner   => 'ubuntu',
  group   => 'ubuntu',
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

# Redo the task #0 but by using Puppet:

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/shared/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/test/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "Holberton School Puppet\n",
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  replace => 'yes',
  owner   => 'ubuntu',
  group   => 'ubuntu',
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

# Redo the task #0 but by using Puppet:

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/shared/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/test/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "Holberton School Puppet\n",
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  replace => 'yes',
  owner   => 'ubuntu',
  group   => 'ubuntu',
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

exec { 'restart nginx':
  command => 'sudo service nginx restart',
}
