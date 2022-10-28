#!/usr/bin/python3
"""create archive module"""
from genericpath import isdir
from fabric.api import *
from datetime import datetime


def do_pack():
    """function to zip files"""
    try:
        new_date = datetime.now()
        new_date = new_date.strftime('%Y%m%d%H%M%S')
        archive = f"versions/web_static_{new_date}.tgz"
        if isdir('versions') is False:
            local('mkdir versions')
        print(f"Packing web_static to {archive}")
        var = local(f'tar -cvzf {archive} web_static')
        return archive
    except Exception:
        return None


def do_deploy(archive_path):
    """new version"""
    env.hosts = ['44.197.231.3', '100.25.4.135']

    if isdir(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as ex:
        return False
