#!/usr/bin/python3
"""This python script distributes an archive to web servers,
using the function do_deploy"""
from os.path import exists
from fabric.api import run, put, env

env.hosts = ["54.144.222.58", "54.237.16.22"]


def do_deploy(archive_path):
    """Deployes the archive to the webserver"""
    if not exists(archive_path):
        return False

    full_name = archive_path.split("/")[1]
    file_name = archive_path.split("/")[1].split(".")[0]

    if put(archive_path, "/tmp/{}".format(
           full_name)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".format(
           file_name)).succeeded is False:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".format(
           file_name)).succeeded is False:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
           full_name, file_name)).succeeded is False:
        return False

    if run("rm /tmp/{}".format(full_name)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(file_name, file_name)
           ).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).succeeded is False:
        return False

    return True
