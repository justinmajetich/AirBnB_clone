#!/usr/bin/python3
""" Deploy archive """
from fabric.api import *
from os import path


def do_deploy(archive_path):
    """ Function deploy  """

    env.user = 'ubuntu'
    env.hosts = ['19.hbtn-cod.io']
    if path.exits(archive_path):

        """ send archive """
        value = put(archive_path, "/tmp/")
        if value.failed:
            return False

        filename = archive_path.split('/')[-1].split('.')[0]
        path_file = "/data/".apend(filename)

        """ uncompress file """
        run("mkdir -p /data/web_static/releases/")
        value = run(
            "tar -xzf {} -C /data/web_static/releases/".format(path_file))
        if value.failed:
            return False

        """ delete tmp file """
        value = run("rm {}".format(path_file))
        if value.failed:
            return False

        """ softlink to new deploy """
        run("rm /data/web_static/current")
        value = run(
            "ln -sf /data/web_static/releases/{}\
                /data/web_static/current".format(filename))
        return True
    else:
        return False
