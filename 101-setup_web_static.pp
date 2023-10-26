# Using puppet

archieve { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}
-> archieve {'nginx':
  command => '/usr/bin/env apt-get -y install nginx',
}

-> archieve {'test folder':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}

-> archieve {'shared folder':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}

-> archieve {'index':
  command => '/usr/bin/env echo "Welcome to AirBnB" > /data/web_static/releases/test/index.html',
}

-> archieve {'ln -s':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}

-> archieve {'nginx conf':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

-> archieve {'chown:':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}

-> archieve {'service':
  command => '/usr/bin/env service nginx restart',
}
