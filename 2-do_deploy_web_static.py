#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.196.60.116', '54.221.176.56']



def do_deploy(archive_path):
    """ fabric script to deploy to a server """
    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")
    filename = filename[1]
    fname = filename.split('.')
    fname = fname[0]

    newpath = '/data/web_static/releases/{}/'.format(fname)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(newpath))
        run("tar -xzf /tmp/{} -C {}".format(filename, newpath))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(newpath, newpath))
        run("rm -rf {}web_static".format(newpath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newpath))
        return True
    except Exception:
        return False
