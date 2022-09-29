#!/usr/bin/python3
"""
Fabric script to Create and distribute an archive to the servers,
using function deploy
"""
from fabric.api import *
from os import path

env.user = 'ubuntu'
env.hosts = ['35.173.36.123', '3.237.39.37']
env.key_filename = "~/id_rsa"


def do_deploy(archive_path):
    """deploys an archive to the servers"""
    if path.exists(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")
        folder = arc[1].strip('.tgz')
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}".format(folder))
        main_f = "/data/web_static/releases/{}".format(base)
        sudo("tar -xzf /tmp/{} -C {}/".format(archive[1], main_f))
        sudo("rm /tmp/{}".format(archive[1]))
        sudo("mv {}/web_static/* {}".format(main_f, main_f))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/ "/data/web_static/current"".format(main_f))
        return True
    except Exception:
        return False
