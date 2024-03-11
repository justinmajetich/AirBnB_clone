#!/usr/bin/python3
"""
A fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["18.214.87.211", "54.157.135.59"]


def do_pack():
    """
    This creates a tgz archive from the contents of web_static.

    Returns:
        Archive path, otherwise None
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    print("Packing web_static to {}".format(file))
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    print("web_static packed: {} -> {}Bytes".format(
        file,
        os.path.getsize(file)
        )
    )
    return file


def do_deploy(archive_path):
    """
    Distributes an archive to web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        True if all operations have been done correctly, otherwise False.
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
    print('New version deployed!')
    return True


def deploy():
    """
    This create and distribute an archive to web servers.

    Returns:
        False if no archive has been created, otherwise the return value
        of do_deploy.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
