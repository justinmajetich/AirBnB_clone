#!/usr/bin/python3
"""3-deploy_web_static module"""
from os.path import isfile
from datetime import datetime
from fabric.api import *

env.hosts = ["35.237.54.178", "35.196.248.176"]


def do_pack():
    """Generates a .tgz archive from the contents of web_static folder of
    AriBnB Clone repo
    Returns: Archive path, otherwise False
    """
    ct = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    local("tar -cvzf versions/web_static_{}.tgz web_static".format(ct))
    if isfile("versions/web_static_{}.tgz".format(ct)):
        return "versions/web_static_{}.tgz".format(ct)


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    archive_path: Path to archive
    Returns: True if all operations done sucessful, otherwise False
    """
    if isfile(archive_path) is False:
        return False

    file_ne = archive_path.split('/')[1].split('.')[0]
    file_np = archive_path.split('/')[1]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(file_ne))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file_np, file_ne))
        run("rm /tmp/{}".format(file_np))
        run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(file_ne, file_ne))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(file_ne))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
/data/web_static/current".format(file_ne))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to web servers
    Returns: Value of do_deploy, False if no archive created
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
