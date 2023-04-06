#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function do_pack and do_deploy.
"""

import os
from fabric.api import env, put, run, local
from datetime import datetime


env.hosts = ['54.158.79.124', '54.146.64.149']


def do_pack():
    """
    Pack the contents of the web_static folder into a .tgz archive
    and store it in the versions directory.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path


def do_deploy(archive_path):
    """
    Deploy the archive to the web server(s)
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """
    Creates and distributes an archive to your web servers.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    result = do_deploy(archive_path)

    return result
