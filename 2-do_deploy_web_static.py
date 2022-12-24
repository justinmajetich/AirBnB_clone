#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['35.175.132.172', '52.91.116.127']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys """

    try:
        if not path.exists(archive_path):
            raise Exception
        file_name_tgz = archive_path.split('/')[-1]
        file_name = file_name_tgz.split('.')[0]
        releases_path = "/data/web_static/releases/{}/".format(file_name)
        tmp_path = "/tmp/{}".format(file_name_tgz)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
