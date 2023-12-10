#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, run, put
from os.path import exists

env.hosts = ['<18.210.15.7>', '<54.160.102.195>']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/
        archive_filename = archive_path.split('/')[-1]
        release_path = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(archive_filename))

        # Create a symbolic link
        run('rm -f /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
