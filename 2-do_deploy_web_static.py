#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import *
import os
from datetime import datetime


env.hosts = ['107.23.93.54', '34.202.233.91']


def do_pack():
    """
    generates a .tgz archive
    from the contents of the web_static folder
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))
    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
    deployes web static 1
    """
    if os.path.exists(archive_path):
        file_name = archive_path.split('/')[1]
        file_path = '/data/web_static/releases/'
        releases_path = file_path + file_name[:-4]
        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}'.format(releases_path))
            run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
            run('rm -rf /tmp/{}'.format(file_name))
            run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
            run('rm -rf {}/web_static'.format(releases_path))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(releases_path))
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False
