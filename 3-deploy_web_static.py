#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers"""
from datetime import datetime
from fabric.api import local, put, run, env
import os


env.user = 'ubuntu'
env.hosts = ['34.74.9.128', '100.24.7.2']


def do_pack():
    """
    To geberate a tgz
    """
    now = datetime.now()
    path_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                              now.month,
                                                              now.day,
                                                              now.hour,
                                                              now.minute,
                                                              now.second)
    local("mkdir -p versions")
    file = local("tar -vczf {} web_static".format(path_file))
    if file.succeeded:
        return(path_file)
    else:
        return None


def do_deploy(archive_path):
    """Write a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers"""
    if not archive_path:
        return False

    file_name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}".format(file_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(file_name, file_name))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(file_name, file_name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(file_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        print("New version deployed")
        return(True)
    except BaseException:
        return(False)


def deploy():
    """deploy"""
    try:
        path = do_pack()
    except BaseException:
        return(False)
    do_deploy(path)
