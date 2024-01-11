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
    serv_archive_path = archive_path.split("/")[-1]
    archive_name = serv_archive_path.strip(".tgz")
    if not put(
        archive_path,
        "/tmp/{}".format(serv_archive_path),
        use_sudo=True,
    ):
        return False
    if sudo(
        "mkdir -p /data/web_static/releases/{}".format(archive_name),
    ).failed:
        return False
    print(serv_archive_path)
    if sudo(
        "tar -xvf /tmp/{} -C /data/web_static/releases/{}".format(
            serv_archive_path, archive_name
        ),
    ).failed:
        return False
    if sudo(
        "mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}".format(
            archive_name, archive_name
        ),
    ).failed:
        return False
    if sudo("rm -rf /tmp/{}".format(serv_archive_path)).failed:
        return False
    if sudo("rm -rf /data/web_static/current").failed:
        return False
    if sudo(
        "ln -sf /data/web_static/releases/{} /data/web_static/current".format(
            archive_name
        ),
    ).failed:
        return False

    print("New version deployed!")
    return True
