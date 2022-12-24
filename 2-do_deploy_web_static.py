#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack."""
from fabric.api import env, put, run
from os import path

env.hosts = ['35.175.132.172', '52.91.116.127']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """that distributes an archive to your web servers"""
    try:
        if not path.exists(archive_path):
            raise Exception
        file_name_tgz = archive_path.split('/')[-1]
        file_name = file_name_tgz.split('.')[0]
        release_path = "/data/web_static/releases/{}/".format(file_name)
        tmp_path = "/tmp/{}".format(file_name_tgz)
        static_current = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(tmp_path, release_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf {}".format(static_current))
        run("ln -s {} {}".format(release_path, static_current))
        print("New version deployed!")
        return True
    except Exception:
        return False
