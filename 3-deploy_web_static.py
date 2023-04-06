#!/usr/bin/env python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function do_pack and do_deploy.
"""

import os
from fabric.api import env, put, run
from datetime import datetime


env.hosts = ['54.158.79.124', '54.146.64.149']


def do_pack():
    """
    Pack the contents of the web_static folder into a .tgz archive
    and store it in the versions directory.
    """
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        local("tar -cvzf {} web_static/".format(archive_path))

        return archive_path

    except:
        return None


def do_deploy(archive_path):
    """
    Deploy the archive to the web server(s)
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = archive_filename.split(".")[0]
        remote_path = "/tmp/{}".format(archive_filename)
        releases_path = "/data/web_static/releases/{}".format(archive_no_ext)

        put(archive_path, remote_path)
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}/".format(remote_path, releases_path))
        run("rm {}".format(remote_path))
        run("mv {}/web_static/* {}/".format(releases_path, releases_path))
        run("rm -rf {}/web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))

        return True

    except:
        return False


def deploy():
    """
    Creates and distributes an archive to your web servers.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    result = do_deploy(archive_path)

    return result
