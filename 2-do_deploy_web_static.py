#!/usr/bin/python3
""" Deploy archive """
from fabric.api import *
from os.path import exists
from fabric.network import disconnect_all
env.user = 'ubuntu'
env.hosts = ['35.243.178.160', '35.243.142.199']


def do_deploy(archive_path):
    """deploy and uncompress file to server."""
    if not exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    name_of_file = archive_path.split('/')[-1]
    name = name_of_file.split('.')[0]
    final_path = "/data/web_static/releases/" + name
    run("mkdir -p " + final_path)
    run("tar -xzf /tmp/" + name_of_file + " -C " + final_path)
    run("rm /tmp/" + name_of_file)

    run("mv " + final_path + "/web_static/* " + final_path)
    run("rm -rf " + final_path + "/web_static/")
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(final_path))

    disconnect_all()

    return True
