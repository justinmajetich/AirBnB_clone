#!/usr/bin/python3
"""
Deploy archive!
"""
from os import path
from fabric.api import env, put, run

env.hosts = ["54.167.24.215", "54.82.159.235"]


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers,
    using the function do_deploy
    """

    if not path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        print(file)

        archieve = file.split(".")[0]
        print(archieve)

        location = "/data/web_static/releases/" + archieve
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(archieve))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file, archieve))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(archieve, archieve))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archieve))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archieve))
        return True

    except Exception:
        return False
