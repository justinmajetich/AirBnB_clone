#!/usr/bin/python3
"""
    a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers, using
    the function do_deploy:
"""

from os.path import exists
from datetime import datetime as dt
from fabric.api import local, put, run, env

env.hosts = ['34.203.33.172', '54.210.234.151']


def do_deploy(archive_path):
    """ a function that distributes an archive to web servers """

    if exists(archive_path) is not True:
        return False
    try:
        archName = archive_path.split("/")[-1]
        Fname = archName.split(".")[0]

        location = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(location, Fname))
        
        #
        run('tar -xzf /tmp/{} -C {}{}/'.format(archName, location, Fname))
        run('rm /tmp/{}'.format(archName))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(location, Fname))
        run('rm -rf {}{}/web_static'.format(location, Fname))
        run('rm -rf /data/web_static/current')

        #
        run('ln -s {}{}/ /data/web_static/current'.format(location, Fname))

        return True
    except:
        return False

