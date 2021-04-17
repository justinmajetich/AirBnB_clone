#!/usr/bin/python3
""" Fabric script """
from fabric.api import env, put, run, local
from datetime import datetime
import os


env.hosts = ['35.231.66.1', '54.221.2.88']


def do_pack():
    """ Generates a .tgz file from the contents of 'web_static' folder"""
    now = datetime.now()
    local('mkdir -p versions')
    result = local('tar -cvzf versions/web_static_{}.tgz ./web_static/'.format(
        now.strftime('%Y%m%d%H%M%S')))
    if result.succeeded:
        return 'versions/web_static_{}.tgz web_static/'.format(
            now.strftime('%Y%m%d%H%M%S'))
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to the servers """
    if not os.path.exists(archive_path):
        return False

    dest_dir = '/data/web_static/releases/'
    aux = archive_path.split('/')[1]
    file_name = aux.split('.')[0]
    dest_file = dest_dir + file_name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest_file))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(file_name, dest_file))
        run('rm -f /tmp/{}.tgz'.format(file_name))
        run('mv {}/web_static/* {}/'.format(dest_file, dest_file))
        run('rm -rf {}/web_static/*'.format(dest_file))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest_file))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ Uses above functions for full deployment """
    file_path = do_pack()
    if file_path is None:
        return False
    val = do_deploy(file_path)
    return val
