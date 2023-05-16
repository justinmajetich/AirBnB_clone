#!/usr/bin/python3
""" Function that deploys """
from datetime import datetime
from fabric.api import *
import os
import shlex


env.hosts = ["54.236.48.165", "100.25.192.36"]
env.user = "ubuntu"


def deploy():
    """DEPLOYS"""
    try:
        archive_path = do_pack()
    except ValueError:
        return False

    return do_deploy(archive_path)


def do_pack():
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = "versions/web_static_{}.tgz".format(t.strftime(f))
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except ValueError:
        return None


def do_deploy(archive_path):
    """Deploys"""
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace("/", " ")
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace(".", " ")
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(releases_path))
        sudo("tar -xzf {} -C {}".format(tmp_path, releases_path))
        sudo("rm {}".format(tmp_path))
        sudo("mv {}web_static/* {}".format(releases_path, releases_path))
        sudo("rm -rf {}web_static".format(releases_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except ValueError:
        return False
