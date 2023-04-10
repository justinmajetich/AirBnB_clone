#!/usr/bin/python3
"""
This script creates a compressed archive of
a given folder and deploys it to web servers.
The archive is named based on the current date and time.
"""

import os
from fabric.api import local, env, put, run, sudo
from datetime import datetime
from fabric.contrib.files import exists


env.hosts = ['54.237.210.251', '54.237.14.69']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    tmp_file = "/tmp/" + file_name
    rel_path = "/data/web_static/releases/" + name
    run("mkdir -p {}".format(rel_path))
    if put(archive_path, tmp_file).failed:
        return False
    if run("tar -xzf {} -C {}".
           format(tmp_file, rel_path)).failed:
        return False
    if run("rm {}".format(tmp_file)).failed:
        return False
    if run("mv {}/web_static/* {}".format(rel_path, rel_path)).failed:
        return False
    if run("rm -rf {}/web_static".format(rel_path)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s {} /data/web_static/current".
           format(rel_path), True).failed:
        return False
    return True
