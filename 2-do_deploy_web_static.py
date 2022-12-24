#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack."""
from fabric.api import env, put, run
from os import path

env.host = ['52.91.116.127', '100.25.45.223']
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
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -c {}".format(tmp_path, release_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
