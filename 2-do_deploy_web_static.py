#!/usr/bin/python3
"""Fab file for task 2 Do Deploy"""
from fabric.api import put, env, sudo
import os

env.hosts = ["18.234.129.112", "35.174.184.68"]
env.warn_only = True


def do_deploy(archive_path: str):
    """
    Distributes an archive to web server.
    Params:
        archive_path: path of the archive to deploy to server
    Return:
        False if archive_path doesnt exist
    """
    if not os.path.exists(archive_path):
        return False
    archive_name = archive_path.strip(".tgz")
    if not put("archive_path", "/tmp/", use_sudo=True):
        return False
    if not sudo(
        "tar -xvf /tmp/{} /data/web_static/releases/{}".format(
            archive_path, archive_name
        ),
    ):
        return False
    if not sudo("rm /tmp/{}".format(archive_path)):
        return False
    if not sudo("rm /data/web_static/current"):
        return False
    if not sudo(
        "ln -sf /data/web_static/releases/{} /data/web_static/current".format(
            archive_name
        ),
    ):
        return False

    return True
