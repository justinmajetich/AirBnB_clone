#!/usr/bin/python3
""" Fabric script, distributes an archive to your
web servers, using the function do_deploy: """

from fabric.api import *
from fabric.operations import *
from os import path
import os.path
import os


env.user = ['ubuntu']
env.hosts = ['34.75.252.164', '35.237.149.147']


def do_deploy(archive_path):
    """ Prototype do_deploy """

    if (path.exists(archive_path) is not True):
        return False
    Directory = archive_path.replace(".tgz", "")
    put("archive_path", "/tmp/{}".format(archive_path))
    run("mkdir -p /data/web_static/releases/{}/".format(Directory))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(archive_path, Directory))
    run("rm /tmp/{}/".format(archive_path))
    run("mv /data/web_static/releases/{}/* /data/web_static/releases/{}/"
        .format(Directory, Directory))
    run("rm -rf /data/web_static/releases/{}/web_static"
        .format(Directory))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(Directory))
    print("New version deployed!")
    return True
