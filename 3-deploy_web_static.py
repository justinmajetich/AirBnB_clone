#!/usr/bin/python3
# Compress before sending
"""Compress usign fabric -- all in one"""
from fabric.api import sudo, env, put, local
import os
import datetime


env.hosts = ['54.209.141.133', '100.26.221.3']


def do_pack():
    """compress function"""
    try:
        local("mkdir -p versions")
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except Exception:
        return None


archive_path = do_pack()


def deploy():
    """deploy archive to server"""
    if not os.path.isfile(archive_path):
        return False
    try:
        name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(name))
        sudo('rm -rf /data/web_static/releases/{}'.format(name[0:-4]))
        sudo('mkdir -p /data/web_static/releases/{}'.format(name[0:-4]))
        sudo('tar -xzvf /tmp/{} -C /data/web_static/releases/{}'.format(name,
             name[0:-4]))
        sudo("mv -f /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}".format(name[0:-4],
             name[0:-4]))
        sudo('rm -f /tmp/{}'.format(name))
        sudo('rm -f /data/web_static/current')
        sudo("ln -sf /data/web_static/releases/{} \
        /data/web_static/current".format(name[0:-4]))
        return True
    except Exception:
        return False
