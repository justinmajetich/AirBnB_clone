#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import run, env, put, local, task
import os

env.hosts = ['54.236.30.207', '3.85.168.24']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
    Deploy package to remote server.

    Arguments:
        archive_path: Path to archive to deploy.
    """
    if not archive_path or not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp')

    ar_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        if not os.path.exists(archive_path):
            return False

        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))

        print("New version deployed!")
        return True

    except Exception:
        return False