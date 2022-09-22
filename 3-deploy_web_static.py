#!/usr/bin/python3
# Full deploy
import os.path
from datetime import datetime
from fabric.contrib import files
from fabric.api import env, put, run, local

env.hosts = ['34.202.231.144', '54.85.119.117']
env.user = 'ubuntu'


def do_pack():
    """
    Create a .tgz archive of the local directory web_static
    """
    time = datetime.utcnow()
    path_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second)
    if os.path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local('tar -cvzf {} web_static'.format(path_file)).failed is True:
        return None

    return path_file


def do_deploy(archive_path):
    """Distributes an archive to a web server

    Args:
        archive_path (str): The path of the compress archive to deploy
    Returns:
        If all operations have been done correctly - True
        Otherwise - False
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    filename = file.split('.')[0]

    if files.exists('/data/web_static/releases/{}/'.format(filename)):
        # print("the '{}' file is already deployed!".format(archive_path))
        return False
    if put(archive_path, '/tmp/{}'.
           format(file)).failed is True:
        return False
    if run('mkdir -p /data/web_static/releases/{}'.
           format(filename)).failed is True:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
           format(file, filename)).failed is True:
        return False
    if run('rm /tmp/{}'.
           format(file)).failed is True:
        return False
    if run('mv /data/web_static/releases/{}/web_static/* '
           '/data/web_static/releases/{}/'.
           format(filename, filename)).failed is True:
        return False
    if run('rmdir /data/web_static/releases/{}/web_static'.
           format(filename)).failed is True:
        return False
    if run('rm /data/web_static/current').failed is True:
        return False
    if run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.
           format(filename)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to web_servers"""
    path_file = do_pack()
    if path_file is None:
        return False
    return do_deploy(path_file)
