# everything in task 0 but in puppet

exec { 'apt_update':
  command     => 'apt-get -y update',
  refreshonly => true,
}

exec { 'install_nginx':
  command => 'sudo apt-get -y install nginx',
  require => Exec['apt_update'],
}

exec { 'start_nginx':
  command => 'sudo service nginx start',
  require => Exec['install_nginx'],
}

exec { 'make_dirs':
  command => 'sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/',
}

exec { 'echo_hol':
  command => 'echo "Holberton School for the win!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
  require => Exec['make_dirs'],
}

exec { 'ln':
  command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
  require => Exec['echo_hol'],
}

exec { 'chown':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  require => Exec['ln'],
}

file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  require => Exec['chown'],
}

$NEW_STRING = "\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

exec { 'sed':
  command => 'sudo sed -i "38i ${NEW_STRING}" /etc/nginx/sites-available/default',
  require => Exec['make_dirs'], # Ensure directories are created before modifying the file
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  require => Exec['sed'],
}
