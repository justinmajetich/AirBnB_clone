# puppet manifest preparing a server for static content deployment
exec { 'Update server':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'Install NGINX':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'Creates directory release/test':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'Creates directories shared':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'Write Hello World in index with tee command':
  command => '/usr/bin/env echo "Hello Wolrd Puppet" | sudo tee /data/web_static/releases/test/index.html',
}
-> exec {'Create Symbolic link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'Change owner and group like ubuntu':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
-> exec {'Add new configuration to NGINX':
  command => '/usr/bin/env sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'Restart NGINX':
  command => '/usr/bin/env service nginx restart',
}
