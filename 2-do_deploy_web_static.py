#!/usr/bin/python3
"""
Deploy archive!
"""
from os import path
from fabric.api import env, put, run

env.hosts = ["34.231.110.206", "3.239.57.196"]


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that distributes an
    archive to your web servers, using the function do_deploy
    """
    if not path.exists(archive_path):
        return False

    file = archive_path.split("/")[-1]
    archieve = file.split(".")[0]
    load = "/tmp/{}".format(file)

    if put(archive_path, load).failed:
        return False

    present = '/data/web_static/releases/{}'.format(archieve)
    if run("rm -rf {}".format(present)).failed:
        return False

    if run("mkdir -p {}".format(present)).failed:
        return False

    change_file = "tar -xzf /tmp/{} -C {}".format(
        file, present
    )
    if run(change_file).failed:
        return False

    remove_file = "rm -f /tmp/{}".format(file)
    if run(remove_file).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    mv_file = "ln -s {} /data/web_static/current".format(present)
    if run(mv_file).failed:
        return False
    return True
