#!/bin/bash

# Define the path to the archive
archive_path="tmp/web_static_20240202033225.tgz"

# Define the two IP addresses
ip_address1="107.23.93.54"
ip_address2="34.202.233.91" 

# Function to deploy web static content
function do_deploy() {
    archive_path=$1
    ip_address=$2

        echo "Deploying to $ip_address..."
        file_name=$(basename $archive_path)
        file_path="/data/web_static/releases/"
        releases_path=$file_path${file_name%.tar.gz}

        ssh -i ~/.ssh/school ubuntu@$ip_address <<EOF
            mkdir -p $releases_path
            tar -xzf $archive_path -C $releases_path
            rm -rf $archive_path
            rm -rf /data/web_static/current
            ln -s $releases_path /data/web_static/current
            echo 'New version deployed!'
EOF
}

# Deploy to the first IP address
do_deploy $archive_path $ip_address1

# Deploy to the second IP address
do_deploy $archive_path $ip_address2
