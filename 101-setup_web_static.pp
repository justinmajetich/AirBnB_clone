# Redo the task #0 but by using Puppet:
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	index index.html index.htm;

	location /hbnb_static{
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 http://cuberule.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}"
package {'nginx':
    ensure => 'present',
    provider => 'apt'
} ->
file {'/data':
    ensure => 'derectory'
} ->
file {'/data/web_static':
    ensure => 'diretory'
} ->
file {'/data/web_static/releases':
    ensure => 'diretory'
} ->
file {'/data/web_static/releases/test':
    ensure => 'diretory'
} ->
file {'/data/web_static/shared':
    ensure => 'diretory'
} ->
file {'/data/web_static/releases/test/index.html':
    ensure => 'present',
    content => 'Holberton School'
} ->
file {'/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test'
} ->
exec {'chown -R ubuntu:ubuntu /data/':
    path => '/usr/bin/:/usr/local/bin:/bin/'
}
file {'/var/www':
    ensure => 'diretory'
} ->
file {'/var/www/html':
    ensure => 'diretory'
} ->
file {'/var/www/html/index.html':
    ensure  => 'present',
    content => "Holberton School\n"
} ->
file {'/var/www/html/404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page\n"
} ->
file {'/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => $nginx_conf
} ->
exec {'nginx restart:
    path => /etc/init.d/'
}
