#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import *
from fabric.context_managers import cd
import os
from datetime import datetime


env['hosts'] = ['107.23.93.54', '34.202.233.91']
env['user'] = 'ubuntu'
env['key_filename'] = '~/.ssh/school'


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
            with cd("/tmp/"):
                put(archive_path, '/tmp/')
            run(f'mkdir -p {releases_path}')
            run(f'tar -xzf /tmp/{file_name} -C {releases_path}')
            run(f'rm -rf /tmp/{file_name}')
            run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
            run('rm -rf {}/web_static'.format(releases_path))
            run('rm -rf /data/web_static/current')
            run(f'ln -s {releases_path} /data/web_static/current')
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False
