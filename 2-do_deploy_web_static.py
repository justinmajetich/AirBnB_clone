#!/usr/bin/python3
"""Fabric script that distributes an archive
to your web servers, using the function do_deploy"""

from fabric.api import local, put, env, run
from os import path
env.hosts = ['34.73.167.126', '35.243.203.71']
env.user = "ubuntu"


def do_deploy(archive_path):
    """function to distribute an archive to web server"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split('/')[1].split('.')[0]
        run("sudo mkdir -p /data/web_static/releases/{}".format(name))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(name, name))
        run("sudo rm /tmp/{}.tgz".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False
