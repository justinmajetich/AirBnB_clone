# Write a Puppet script that sets up your web servers for the deployment of web_static. It must:
#   Install Nginx if it not already installed
#   Create the folder /data/ if it doesn’t already exist
#   Create the folder /data/web_static/ if it doesn’t already exist
#   Create the folder /data/web_static/releases/ if it doesn’t already exist
#   Create the folder /data/web_static/shared/ if it doesn’t already exist
#   Create the folder /data/web_static/releases/test/ if it doesn’t already exist
#   Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
#   Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
#   Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
#   Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
#   Use alias inside your Nginx configuration
#   Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

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

exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  refreshonly => true,
}
