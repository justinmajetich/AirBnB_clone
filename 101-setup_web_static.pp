# Puppet command for task 0
exec { 'Update bash':
  command  => 'sudo apt-get update',
  provider => shell
}
exec { 'Install NGINX':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  require  => Exec['Update bash']
}
exec { 'Create shared path':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  require  => Exec['Install NGINX']
}
exec { 'Create test path':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  require  => Exec['Create shared path']
}
exec { 'Adding fake HTML':
  command  => 'echo "FakeHTML" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  require  => Exec['Create test path'],
  returns  => [0, 1]
}
exec { 'Symbolic link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  require  => Exec['Adding fake HTML']
}
exec { 'Permissions':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell,
  require  => Exec['Symbolic link']
}
exec { 'Adding location':
  command  => 'sudo sed -i "29i\\\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Exec['Permissions']
}
exec { 'Restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Exec['Adding location']
}
