#!/usr/bin/python3
""" Fabric script, distributes an archive to your
web servers, using the function do_deploy: """

from fabric.api import *
import os.path
from os import path

env.user = ['ubuntu']
env.hosts = ['34.75.252.164', '35.237.149.147']


def do_deploy(archive_path):
    """ func to distribute archive """
    """ run("do_deploy") """

    if (path.exists(archive_path) is not True):
        return False

    archive_p = archive_path
    archive_folder = archive_path.replace(".tgz", "")

    put("archive_path", "/tmp/{}".format(archive_p))
    run("mkdir -p /data/web_static/releases/{}/".format(archive_folder))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(archive_p, archive_folder))
    run("rm /tmp/{}/".format(archive_path))
    run("mv /data/web_static/releases/{}/* /data/web_static/releases/{}/"
        .format(archive_folder, archive_folder))
    run("rm -rf /data/web_static/releases/{}/web_static"
        .format(archive_folder))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(archive_folder))
    print("New version deployed!")
    return True
