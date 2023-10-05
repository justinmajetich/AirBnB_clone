#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
and deploys it using the function do_deploy.
"""

from fabric.api import env, run, put
import os

env.hosts = ['54.172.84.26', '52.23.177.182']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(archive_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(archive_filename, archive_no_ext))
        run("rm /tmp/{}".format(archive_filename))
        run("mv / data/web_static/releases/{}/web_static/*
            / data/web_static/releases/{} /"
            .format(archive_no_ext, archive_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(archive_no_ext))

        return True

    except Exception as e:
        return False
