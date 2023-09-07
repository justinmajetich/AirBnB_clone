# 

exec { 'update':
  command  => 'sudo apt-get -y update',
}

exec { 'install Nginx':
  command  => 'sudo apt-get -y install nginx',
  require  => Exec['update'],
}

exec { 'start Nginx':
  command  => 'sudo service nginx start',
  require  => Exec['install Nginx'],
}

exec { 'create first directory':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  require  => Exec['start Nginx'],
}

exec { 'create second directory':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  require  => Exec['create first directory'],
}

exec { 'content into html':
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  require  => Exec['create second directory'],
}

exec { 'symbolic link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  require  => Exec['content into html'],
}

exec { 'put location':
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  require  => Exec['symbolic link'],
}

exec { 'restart Nginx':
  command  => 'sudo service nginx restart',
  require  => Exec['put location'],
}

file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  require => Exec['restart Nginx'],
}
