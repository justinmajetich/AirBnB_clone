#!/usr/bin/python3
"""deploy files"""
from os.path import exists
from fabric.api import run, env, put,  local
from datetime import datetime
import os
env.hosts = ['54.91.171.75', '54.234.45.172']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except Exception:
        return None


def do_deploy(archive_path):
    """deploy web static"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(path_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, path_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(path_name, path_name))
        run("rm -rf {}/web_static".format(path_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(path_name))
        return True
    except Exception:
        return False


def deploy():
    """deploy files"""
    archive = do_pack()
    if not exists(archive):
        return False
    return do_deploy(archive)
