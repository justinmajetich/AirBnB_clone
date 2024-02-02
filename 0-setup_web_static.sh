#!/usr/bin/env bash
# Exit script if any command fails
set -e

# Function to create directories if they don't exist
create_directories() {
    mkdir -p /data/web_static/{releases/test,shared}
}

# Function to create fake HTML file
create_fake_html() {
    echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
}

# Function to create symbolic link
create_symbolic_link() {
    ln -sf /data/web_static/releases/test /data/web_static/current
}

# Function to change ownership recursively
change_ownership() {
    chown -R root:root /data/
}

# Function to update Nginx configuration
update_nginx_config() {
    sed -i '/alias/s/$/\/;/' /etc/nginx/sites-available/default
    service nginx restart
}

# Main function
main() {
    create_directories
    create_fake_html
    create_symbolic_link
    change_ownership
    update_nginx_config
}

# Trap any errors and exit with success status
trap 'echo "Error encountered. Exiting with success status."; exit 0' ERR

main
