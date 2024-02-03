# everything in task 0 but in puppet

exec { 'apt_update':
  provider    => shell,
  command     => 'apt-get -y update',
  refreshonly => true,
}

exec { 'install_nginx':
  command => 'sudo apt-get -y install nginx',
}

exec {'start nginx':
  provider => shell,
  command  => 'sudo service nginx start',
}

exec { 'make_dirs':
  command => 'sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/',
}

exec { 'echo_hol':
  command => 'echo "Holberton School for the win!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}

exec { 'ln':
  command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
}

exec { 'chown':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  before  => Exec['echo_hol'],
}

$NEW_STRING="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

exec { 'sed':
  provider => shell,
  command => 'sudo sed -i "38i $NEW_STRING" /etc/nginx/sites-available/default',
}

exec { 'restart':
  command => 'sudo service nginx restart',
}
