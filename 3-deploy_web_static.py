#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
and deploys it using the function deploy.
"""

from fabric.api import env, run, put
from os.path import exists
from datetime import datetime
import os

env.hosts = ['54.172.84.26', '52.23.177.182']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Create a compressed archive of the web_static folder"""
    try:
        now = datetime.now()
        archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it"""
    if not exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_no_ext))
        run("rm /tmp/ {}".format(archive_filename))
        run("mv / data/web_static/releases/{}/web_static/*
            / data/web_static/releases/{} /"
            .format(archive_no_ext, archive_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_no_ext))

        return True

    except Exception:
        return False


def deploy():
    """
    Deploys the web_static archive to the web servers.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
