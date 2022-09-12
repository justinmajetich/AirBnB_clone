# Script that configures Nginx server with some folders and files

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['start Nginx'],
}

exec {'start Nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['create first directory'],
}

exec {'create first directory':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['create second directory'],
}

exec {'create second directory':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['content into html'],
}

exec {'content into html':
  provider => shell,
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['symbolic link'],
}

exec {'symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['put location'],
}

exec {'put location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
