#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import local, env, run, put
from fabric.api import task, local
from datetime import datetime
import os


env.hosts = ['54.237.91.183', '54.173.37.227']
env.user = 'ubuntu'


@task
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
    if not archive_path or not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp')
    ar_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(ar_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm /tmp/{}.tgz'.format(ar_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            ar_name
        ))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(
            ar_name
        ))
        print("New version deployed!")
        return True
    except Exception:
        return False
