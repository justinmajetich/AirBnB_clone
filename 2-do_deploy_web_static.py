#!/usr/bin/python3
"""
Fabric script that deploys an archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['100.26.20.151', '54.82.197.5']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        (bool): True if all operations are successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, folder_name))
        run('rm /tmp/{}'.format(file_name))
        run('cp -R {0}{1}/web_static/* {0}{1}/'.format(path, folder_name))
        run('rm -rf {}{}/web_static'.format(path, folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, folder_name))
        return True
    except Exception as e:
        print("Error deploying:", e)
        return False
