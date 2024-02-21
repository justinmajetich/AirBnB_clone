#!/usr/bin/env puppet
# lets configure the web server using puppet
$all_dirs = [ '/data/', '/data/web_static/',
                        '/data/web_static/releases/', '/data/web_static/shared/',
                        '/data/web_static/releases/test/'
                  ]

package {'nginx':
  ensure  => installed,
}

file { $all_dirs:
        ensure  => 'directory',
        owner   => 'ubuntu',
        group   => 'ubuntu',
        recurse => 'remote',
        mode    => '0774',
}
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}
file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'This has been tough man!',
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file_line {'AirBnB deploy static':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}",
}

service {'nginx':
  ensure  => running,
}

exec {'/usr/sbin/service  nginx restart':
}