#!/usr/bin/python3
""" Write a Fabric script """
from fabric.api import local, env, run, put
from datetime import datetime
from os.path import exists

env.hosts = ['35.231.190.68', '34.75.255.60']


def do_pack():
    """[summary]"""
    local('mkdir -p versions')
    file_tar = local("tar -czvf versions/web_static_{}.tgz web_static/"
                     .format((datetime.strftime(datetime.now(),
                                                "%Y%m%d%H%M%S"))),
                     capture=True)
    if file_tar.succeeded:
        return file_tar
    return None


def do_deploy(archive_path):
    """[summary]"""
    if exists(archive_path):
        file_path = archive_path.split("/")[1]
        file_srvr = "/data/web_static/releases/{}".format(
            file_path.replace(".tgz", ""))
        put('{}'.format(archive_path), '/tmp/')
        run('mkdir -p {}'.format(file_srvr))
        run('tar -xzf /tmp/{} -C {}/'.format(
            file_path,
            file_srvr))
        run('rm /tmp/{}'.format(file_path))
        run('mv -f {}/web_static/* {}/'.format(file_srvr, file_srvr))
        run('rm -rf {}/web_static'.format(
            file_srvr))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(
            file_srvr))
        return True
    else:
        return False
