### Bypass Method
- clone repo on server.
- mkdir '/var/www/html/hbnb_static/'.
- cp 'alu-AirBnB_clone_v2/web_static/*' to '/var/www/html/hbnb_static/'.
- edit '/etc/nginx/sites-available/default' to serve '/var/www/html/hbnb_static/'.
````
    location /hbnb_static/ {
        root /var/www/html;
    }
````
- restart nginx (sudo service nginx restart).
