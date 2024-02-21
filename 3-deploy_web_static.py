#!/usr/bin/python3
"""
    This script creates and distributes an archive to your web servers,
    using the function deploy
"""
from fabric.api import *
import re
import os
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['3.238.130.141', '44.192.24.10']


def do_pack():
    """
        compresses web_static files into one file
    """
    local("mkdir -p versions")
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_path = "versions/web_static_{}.tgz".format(current_date)
    captured = local("tar -cvzf {} web_static".format(tar_path), capture=True)
    if captured.failed:
        return None
    return tar_path


def do_deploy(archive_path):
    """
        Deploys archive path to remote hosts
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        regex = r'\/(\w+).tgz$'
        pattern = re.findall(regex, archive_path)

        web_path = "/data/web_static/releases/{}".format(pattern[0])

        run("mkdir -p {}".format(web_path))
        # unpacking
        run("tar -xzf /tmp/{}.tgz -C {}".format(pattern[0], web_path))
        run("mv {}/web_static/* {}".format(web_path, web_path))
        run("rm -rf {}/web_static".format(web_path))
        run("rm /tmp/{}.tgz".format(pattern[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(web_path))

        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
        packs and deploys web_static
    """
    archived = do_pack()
    if not archived:
        return False

    return do_deploy(archived)
