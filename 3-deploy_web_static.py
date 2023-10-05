#!/usr/bin/env python3
"""Full deployment"""
from fabric.api import local, env, run, put
from os.path import exists
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/{}/".format(no_ext)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
    except Exception as e:
        print(e)
        return None
