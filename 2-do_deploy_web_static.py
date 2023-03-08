#!/usr/bin/python3
"""deploy web static"""
from fabric.api import run, env, put
from os.path import exists
env.hosts = ['54.91.171.75', '54.234.45.172']


def do_deploy(archive_path):
    """deploy web static"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split("/")[-1].split(".")[0]
        path_name = "/data/web_static/releases/" + name
        run("mkdir -p {}".format(path_name))
        run('tar -xzf /tmp/{} -C {}/'.format(archive_path.split("/")[-1], name))
        run("rm /tmp/{}".format(archive_path.split("/")[-1]))
        run("mv {0}/web_static/* {0}".format(name))
        run("rm -rf {}/web_static".format(name))
        run('rm -rf /data/web_static/current')
        return True
    except:
        return False

