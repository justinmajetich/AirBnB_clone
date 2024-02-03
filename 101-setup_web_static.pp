# everything in task 0 but in puppet

exec { 'apt_update':
  command     => 'apt-get -y update',
} ->

package { 'nginx':
 ensure => 'present',
 provider => 'apt',
} ->

file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
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

exec { 'sudo chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
} ->


$NEW_STRING = "\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

exec { 'sed':
  command => 'sudo sed -i "38i ${NEW_STRING}" /etc/nginx/sites-available/default',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
