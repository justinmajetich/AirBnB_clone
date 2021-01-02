#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Colne repo,
# using the function do_pack
from datetime import datetime
from fabric.api import local
from fabric.api import *
from os.path import isfile

env.user = 'ubuntu'
env.hosts = ['34.75.217.72', '34.73.33.136']


def do_pack():
    """
    that fenerates a .tgz archive from the contents of the web_static folder
    """
    dt = datetime.now()
    file = 'web_static' + str(dt.year) + str(dt.month) + str(dt.day)
    file = file + str(dt.hour) + str(dt.minute) + str(dt.second) + '.tgz'
    local('mkdir -p versions')
    directory = local('tar -cvzf versions/{} web_static'. format(file))
    if directory.failed:
        return None
    return 'versions/{}'.format(file)


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers, using
    the function do_deploy:
    """
    if not isfile(archive_path):
        return False
    put(archive_path, '/tmp/')
    file = archive_path.replace('.tgz', '')
    file = file.replace('versions/', '')
    run('mkdir -p /data/web_static/releases/{}/'.format(file))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(file, file))
    run('rm /tmp/{}.tgz'.format(file))
    run('mv /data/web_static/releases/{}/'.format(file))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(file))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(file))
    print('New version deployed!')
    return True
