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
    """Deploys an archive to a web server"""
    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    basename = os.path.splitext(filename)[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(basename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, basename))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(basename, basename))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(basename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(basename))
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to web servers"""
    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)
