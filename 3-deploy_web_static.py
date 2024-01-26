#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive
to your web servers, using the function deploy
"""
from fabric.api import local, env, run, put
from os import path
from datetime import datetime


env.hosts = ['54.237.91.183', '54.173.37.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Generates a .tgz archive from the
    contents of the web_static folder
    """
    local("mkdir -p versions")
    t = datetime.now()
    t = t.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(t)
    try:
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None


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


def deploy():
    """
    Creates and distributes an archive to your web servers
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
