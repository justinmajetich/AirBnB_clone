#!/usr/bin/python3
""" Deploy archive """
from fabric.api import *
from os.path import exists
from fabric.network import disconnect_all
env.user = 'ubuntu'
env.hosts = ['35.243.178.160', '35.243.142.199']


def do_deploy(archive_path):
    """ Function deploy  """

    if path.exits(archive_path):

        put(archive_path, "/tmp/")
        full_name = archive_path.split('/')[-1]
        name = full_name.split('.')[0]
        final_path = "/data/web_static/releases/" + name
        run("mkdir -p " + final_path)
        run("tar -xzf /tmp/" + full_name + " -C " + final_path)
        run("rm /tmp/" + full_name)

        run("mv " + final_path + "/web_static/* " + final_path)
        run("rm -rf " + final_path + "/web_static/")
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(final_path))

        disconnect_all()

        return True
    else:
        return False
