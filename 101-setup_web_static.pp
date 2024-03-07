# Class: setup_web_static
#
# This class sets up web servers for the deployment of web_static.
#
class setup_web_static {
  $nginx_package_name = 'nginx'
  $web_static_dirs = ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']
  $web_static_current_link = '/data/web_static/current'
  $web_static_test_index = '/data/web_static/releases/test/index.html'
  $nginx_config_file = '/etc/nginx/sites-available/default'

  package { $nginx_package_name:
    ensure => installed,
  }

  file { $web_static_dirs:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { $web_static_test_index:
    ensure  => file,
    content => 'This is a test',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { $web_static_current_link:
    ensure => link,
    target => '/data/web_static/releases/test',
    force  => true,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  exec { 'update_nginx_config':
    command => "sed -i '38i\\\\tlocation /hbnb_static/ {\\\\n\\\\t\\\\talias " +
            "/data/web_static/current/;\\\\n\\\\t}\\\\n' ${nginx_config_file}",
    require => Package[$nginx_package_name],
  }

  service { $nginx_package_name:
    ensure    => running,
    enable    => true,
    subscribe => Exec['update_nginx_config'],
  }
}
