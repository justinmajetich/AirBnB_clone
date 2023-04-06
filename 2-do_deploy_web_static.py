#!/usr/bin/python3
# deploy sending
"""deploy archive usign fabric"""
from fabric.api import sudo, env, put
import os

env.hosts = ['54.209.141.133', '100.26.221.3']


def do_deploy(archive_path):
    """deploy archive to server"""
    if not os.path.isfile(archive_path):
        return False
    try:
        name = archive_path.split('/')[-1]
        put(archive_path, "/tmp/{}".format(name))
        sudo("mkdir -p /data/web_static/releases/{}".format(name[0:-4]))
        sudo(
            "tar -xzvf /tmp/{} -C /data/web_static/releases/{}".format(name, name[0:-4]))
        sudo("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(
            name[0:-4], name[0:-4]))
        sudo("rm -f /tmp/{}".format(name))
        sudo("rm -f /data/web_static/current")
        sudo(
            "ln -sf /data/web_static/releases/{} /data/web_static/current".format(name[0:-4]))
        return True
    except Exception:
        return False
