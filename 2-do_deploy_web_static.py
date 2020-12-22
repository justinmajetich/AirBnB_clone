#!/usr/bin/python3
""" Fabric script, distributes an archive to your
web servers, using the function do_deploy: """

from fabric.api import *
from os import path

env.hosts = ['35.237.149.147', '34.75.252.164']


def do_deploy(archive_path):
    """Deploy in the servers"""
    if not path.exists(archive_path):
        return False

    ufile = put(archive_path, '/tmp/')
    if ufile.failed:
        return False

    complete = archive_path.split("/")[-1]
    fileok = complete.split(".")[0]

    run("mkdir -p /data/web_static/releases/{}/".format(fileok))
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
        format(fileok, fileok))

    run("rm /tmp/{}.tgz".format(fileok))

    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(fileok, fileok))
    run("rm -rf /data/web_static/releases/{}/web_static".
        format(fileok))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
        format(fileok))
    print("New version deployed!")
    return True
