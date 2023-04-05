#!/usr/bin/python3
""" Fabric module """
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run
from datetime import datetime
import os
env.hosts = ['34.234.193.108', '54.165.46.2']
env.usre = 'ubuntu'


def do_pack():
    """Archive the content of web_static folder"""
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_path = "versions/web_static_{}.tgz".format(time)
    cmd = "tar -cvzf {} web_static/*".format(file_path)
    local("mkdir -p versions")
    local(cmd)
    if os.path.exists(file_path):
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """Distribute an Archive to servers"""
    if not os.path.exists(archive_path):
        return false
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]

        put(archive_path, '/tmp/')
        run('mkdir /data/web_static/releases/{}'.format(file_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.
            format(file_name, file_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.
            format(file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_name))
        run('rm -rf /tmp/{}.tgz'.format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.
            format(file_name))
        return True
    except:
        return False
