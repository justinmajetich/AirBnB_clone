#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives,
using the function do_clean
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
    if archive_path:
        if os.path.exists(archive_path):
            archive_name = archive_path[9:-4]
            try:
                with cd("/tmp/"):
                    put(archive_path, '/tmp/')
                run(f'mkdir -p /data/web_static/releases/{archive_name}/')
                part_1 = '/data/web_static/releases/' + archive_name + '/'
                part_2 = '/data/web_static/current'
                run(f'tar -xzf /tmp/{archive_name}.tgz -C {part_1}')
                run(f'rm -rf /tmp/{archive_name}.tgz')
                run('rm -rf /data/web_static/current')
                run(f'ln -s {part_1} {part_2}')
                print('New version deployed!')
            except Exception:
                return False
        else:
            return False
    else:
        return False


def deploy():
    """
    deploys 2
    """
    created_archive = do_pack()
    return do_deploy(created_archive)
