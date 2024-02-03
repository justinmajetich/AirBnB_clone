exec { 'apt_update':
  command     => 'apt-get -y update',
  refreshonly => true,
}

exec { 'install_nginx':
  command => 'sudo apt-get -y install nginx',
  require => Exec['apt_update'],
}

exec { 'make_dirs':
  command => 'sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/',
  require => Exec['install_nginx'],
}

exec { 'echo_hol':
  command => 'echo "Holberton School for the win!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
  require => Exec['make_dirs'],
}

exec { 'rm_f':
  command => 'sudo rm -rf /data/web_static/current',
  require => Exec['echo_hol'],
}

exec { 'ln':
  command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
  require => Exec['rm_f'],
}

exec { 'chown':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  require => Exec['ln'],
}

$NEW_STRING="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

exec { 'sed':
  command => 'sudo sed -i "38i $NEW_STRING" /etc/nginx/sites-available/default',
  require => Exec['chown'],
}

exec { 'start'
  command => 'sudo service nginx restart',
  require => Exec['sed'],
}
