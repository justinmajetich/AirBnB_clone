#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import local, env, run, put
from os import path


env.hosts = ['54.237.91.183', '54.173.37.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.exists(archive_path):
        return False
    try:
        name = archive_path.split("/")[-1]
        name2 = name.split(".")[0]
        put(archive_path, "/tmp/{}".format(name))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name2))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(name, name2))
        run("sudo rm /tmp/{}".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name2))
        return True
    except Exception:
        return False
