#!/usr/bin/env python3
"""
Fabric script to deploy an archive to web servers
"""
import os
from fabric.api import env, run
from fabric.operations import put
from datetime import datetime

env.hosts = ['35.153.232.20', '52.90.15.8']


@runs_once
def do_pack():
    """Generates .tgz archive from web_static dir"""
    local("mkdir -p versions")
    filename = "web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    path = "versions/{}".format(filename)
    result = local("tar -cvzf {} web_static".format(path))

    if result.failed:
        return None
    return path


def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    basename = os.path.splitext(filename)[0]
    releases_dir = "/data/web_static/releases/"
    tmp_dir = "/tmp/"

    try:
        put(archive_path, tmp_dir)
        run("mkdir -p {}{}".format(releases_dir, basename))
        run("tar -xzf {}{} -C {}{}".format(tmp_dir, filename,
                                           releases_dir, basename))
        run("rm {}{}".format(tmp_dir, filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(releases_dir, basename))
        run("rm -rf {}{}/web_static".format(releases_dir, basename))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(releases_dir,
                                                         basename))
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to web servers"""
    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)
