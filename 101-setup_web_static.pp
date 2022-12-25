$data_dirs = ['/data', '/data/web_static', '/data/web_static/releases',
	'/data/web_static/releases/test', '/data/web_static/shared/']

$user = 'ubuntu'

exec {'get update and install nginx and start nginx':
  provider => shell,
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && sudo service nginx star',
}

file {$data_dirs:
	ensure	=> directory,
	group 	=> $user,
	owner 	=> $user,
	mode 		=> 0644
}

file {"/data/web_static/releases/test/index.html":
	ensure 	=> file,
	content => "Hello Friends",
	group 	=> $user,
	owner 	=> $user
}

file { '/data/web_static/current':
	ensure 	=> link,
	target 	=> '/data/web_static/releases/test/',
	force 	=> true
	group 	=> $user,
	owner 	=> $user
}

exec {'put location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default'
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
