# Redo the task #0 but by using Puppet:

# run update 
exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

# Insure Nginx is installed
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

# Create that data directory 
file { '/data/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

# Create that /data/web_static/ directory 
file { '/data/web_static/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

# Create that /data/web_static/releases/ directory 
file { '/data/web_static/releases/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

# Create that /data/web_static/shared/ directory 
file { '/data/web_static/shared/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->

# Create that /data/web_static/releases/test/ directory 
file { '/data/web_static/releases/test/':
    ensure => 'directory',
    group  => 'ubuntu',
    owner  => 'ubuntu',
} ->


# Create that HTML index file in /data/web_static/releases/test/
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "Holberton School Puppet\n",
} ->

# Link /data/web_static/current to /data/web_static/releases/test/
# If link exits; recreate
file { '/data/web_static/current':
  ensure  => 'link',
  replace => 'yes',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  target  => '/data/web_static/releases/test',
} ->

# Give ownership of the /data/ folder to the ubuntu user AND group
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
exec { 'sed':
  command => "sed -i \
  '/^\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
