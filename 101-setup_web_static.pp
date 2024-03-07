# setup_web_static.pp
class setup_web_static {
  package { 'nginx':
    ensure => installed,
  }

  # Define the Nginx configuration
  $nginx_conf = @(END)
  server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root   /var/www/html;
      index  index.html index.htm;

      location /hbnb_static {
          alias /data/web_static/current;
          index index.html index.htm;
      }

      location /redirect_me {
          return 301 https://www.youtube.com/watch?v=3MbaGJN2ioQ;
      }

      error_page 404 /custom_404.html;
      location =/custom_404.html {
        root /var/www/html;
        internal;
      }
  }
  | END

  file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  # Manage symbolic link for current release
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    force  => true,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => $nginx_conf,
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasrestart => true,
  }
}
