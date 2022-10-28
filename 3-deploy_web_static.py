#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_pack():
    """ Write a Fabric script that generates a .tgz archive from the
    contents of the web_static """
    date = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz"\
              .format(date.year, date.month, date.day, date.hour,
                      date.minute, date.second)
    if isdir("versions") is False:
        local("mkdir versions")
    print("Packing web_static to {}".format(archive))
    result = local("tar -vczf {} web_static".format(archive))
    if result.succeeded:
        return (archive)
    else:
        return None


def do_deploy(archive_path):
    """new version"""
    if exists(archive_path) is False:
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


def deploy():
    """archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
