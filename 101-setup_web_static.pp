# puppet manifest preparing a server for static content deployment
exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'b':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'c':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'d':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'e':
  command => '/usr/bin/env echo "Puppet x Holberton School" > /data/web_static/releases/test/index.html',
}
-> exec {'f':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'h':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'i':
  command => '/usr/bin/env service nginx restart',
}
-> exec {'g':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
