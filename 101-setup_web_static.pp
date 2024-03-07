# setup_web_static.pp
class web_static {
  package { 'nginx':
    ensure => installed,
  }

  # Ensure necessary directories exist with proper ownership
  file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Create a test HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => '<html>
                  <head>
                  </head>
                  <body>
                    Holberton School
                  </body>
                </html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  # Manage symbolic link for current release
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    force  => true,  # Remove the file if it already exists and create the symlink
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Update Nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => 'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        add_header X-Served-By $HOSTNAME;

        root /var/www/html;
        index index.html index.htm;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=3MbaGJN2ioQ;
        }

        location /hbnb_static {
            alias /data/web_static/current/;
            index index.html index.htm;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
            root /var/www/html;
            internal;
        }
    }',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and enabled to start at boot
  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasrestart => true,  # Allow Puppet to use the service's restart command
  }
}
