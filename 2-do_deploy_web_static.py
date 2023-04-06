#!/usr/bin/python3
"""
Fabric script to distribute archive to web servers using do_deploy function
"""

import os
from fabric.api import env, put, run, local
from datetime import datetime

env.hosts = ['54.158.79.124', '54.146.64.149']
env.user = 'ubuntu'


def do_pack():
    """Create a compressed archive of web_static contents"""

    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_name = 'web_static_' + now + '.tgz'
    if not os.path.exists('versions'):
        os.mkdir('versions')
    local('tar -czvf versions/{} web_static'.format(archive_name))
    archive_path = 'versions/{}'.format(archive_name)
    if os.path.exists(archive_path):
        return archive_path
    return None


def do_deploy(archive_path):
    """Deploy archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    # Get archive filename (without extension) from path
    filename = os.path.basename(archive_path)
    name = filename.split(".")[0]

    # Upload archive to /tmp/ directory on server
    put(archive_path, "/tmp/{}".format(filename))

    # Create directory to uncompress archive
    run("mkdir -p /data/web_static/releases/{}/".format(name))

    # Uncompress archive to directory
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(filename, name))

    # Remove archive from server
    run("rm /tmp/{}".format(filename))

    # Move contents of uncompressed archive to proper directory
    run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(name, name))

    # Remove old symbolic link if it exists
    run("rm -f /data/web_static/current")

    # Create new symbolic link
    run("ln -s /data/web_static/releases/{}/ \
        /data/web_static/current".format(name))

    return True
