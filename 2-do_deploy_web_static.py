#!/usr/bin/python3
"""
Fabric script that distributes an archive to my web servers
"""

from fabric.api import *
from fabric.operations import run, put, sudo
import os

env.hosts = [ubuntu@54.146.95.43, ubuntu@34.229.67.181]


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Parameters:
        - archive_path(str): Path to the archive path.

    Return:
        - None.
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        folder = archive.split(".")[0]
        new_archive = ".".join(folder)

        put("{}".format(archive_path), "/tmp/{}".format(archive))
        run("mkdir -p {}/{}/".format(path, folder))
        run("tar -xzf /tmp/{} -C {}/{}/".format(new_archive, path, folder))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/".format(path, folder, path, folder))
        run("rm -rf {}/{}/web_static".format(path, folder))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current".format(path, folder))
    except Exception as e:
        print(e)
        return False
    finally:
        return True
