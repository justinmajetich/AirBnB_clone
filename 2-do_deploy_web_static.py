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
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -c {}".format(file_name_tgz, release_path))
        run("mv {}web_static/* {}".format(release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
    except Exception:
        return False
