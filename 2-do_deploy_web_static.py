#!/usr/bin/python3
""" Deploy archive """
from fabric.api import *
from os import path


def do_deploy(archive_path):
    """ Function deploy  """

    env.user = 'ubuntu'
    env.hosts = ['35.243.178.160', '35.243.142.199']
    if path.exits(archive_path):
        full_name = archive_path.split('/')[-1]
        filename = full_name.split('.')[0]

        value = put(archive_path, "/tmp/{}".format(full_name))
        if value.failed:
            return False

        value = run("mkdir -p /data/web_static/releases/{}/".format(filename))
        if value.failed:
            return False

        value = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                    .format(full_name, filename))
        if value.failed:
            return False

        value = run("rm /tmp/{}".format(full_name))
        if value.failed:
            return False

        value = run("mv /data/web_static/releases/{}/web_static/* "
                    "/data/web_static/releases/{}/".format(filename, filename))
        if value.failed:
            return False

        value = run("rm -rf /data/web_static/releases/{}/web_static"
                    .format(filename))
        if value.failed:
            return False

        value = run("rm -rf /data/web_static/current")
        if value.failed:
            return False

        value = run(
            "ln -sf /data/web_static/releases/{}\
                /data/web_static/current".format(filename))
        if value.failed:
            return False
        return True
    else:
        return False
