#!/usr/bin/python3
"""
Deploy archive!
"""
from fabric.api import run, env, put
from os import path

env.hosts = ["34.231.110.206", "3.239.57.196"]


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that distributes an
    archive to your web servers, using the function do_deploy
    """
    if not path.exists(archive_path):
        return False
    try:
        path = archive_path.split("/")[-1]
        print(path)

        archieve = path.split(".")[0]
        print(archieve)

        file_path = "/data/web_static/releases/" + archieve
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(archieve))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path, archieve))
        run("rm /tmp/{}".format(path))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(archieve, archieve))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archieve))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archieve))
        return True

    except Exception:
        return False
