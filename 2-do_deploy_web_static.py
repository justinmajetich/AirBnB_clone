#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy"""

from os.path import exists
from fabric.api import put, run, env


def do_deploy(archive_path):
    """Ditributes an archive file to my web server"""
    if exists(archive_path) is False:
        return False
    try:
        path = "/data/web_static/releases/"
        fileName = archive_path.split("/")[-1]
        noExtFile = fileName.split(".")[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}'.format(path, noExtFile))
        run('tar -xzf /tmp/ {}'.format(fileName))
        run('rm /tmp/{}'.format(fileName))
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, noExtFile))
        run('rm -rf {}{}/web_static'.format(path, noExtFile))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{} /data/web_static/current'.format(path, noExtFile))
        return True
    except:
        return False
