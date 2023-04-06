#!/usr/bin/python3
"""
Fabric script to deploy archive to web servers
"""

import os
from datetime import datetime
from fabric.api import env, put, run

env.hosts = ['35.153.232.20', '52.90.15.8']


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
