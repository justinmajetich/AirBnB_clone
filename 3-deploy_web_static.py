#!/usr/bin/python3

"""
This script hosts a function that packs the content of a file
Deploys a code to a web server
"""


import os
from fabric.api import local, env, put, run, runs_once
from datetime import datetime


"""The list of host server IP addresses"""
env.hosts = ["54.90.49.170", "54.157.191.16"]


@runs_once
def do_pack():
    '''Generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    tgz_pathname = ('versions/web_static_{}.tgz'
                    .format(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')))
    tar_ball_output = local("tar -czvf {} web_static".format(tgz_pathname))
    if tar_ball_output.failed:
        return None
    return tgz_pathname


def do_deploy(archive_path):
    """This method deploys hbnb static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    dir_name = file_name.replace(".tgz", "")
    directory = "/data/web_static/releases/{}/".format(dir_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(directory))
        run("tar -xzf /tmp/{} -C {}".format(file_name, directory))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(directory, directory))
        run("rm -rf {}web_static".format(directory))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(directory))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """
    This function calls the do_pack and do_ deploy method
    """

    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
