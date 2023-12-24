#!/usr/bin/python3
"""web server distribution
    """
from fabric.api import *
import tarfile
import os.path
import re
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ["104.196.155.240", "34.74.146.120"]
env.key_filename = "~/id_rsa"


def do_pack():
    """distributes an archive to your web servers
    """
    target = local("mkdir -p ./versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("./versions/web_static_{}.tgz".format(opt))
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except:
        return False


def deploy():
    """distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    f = do_deploy(path)
    return f
