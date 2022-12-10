#!/usr/bin/python3
"""Generate a .tgz archive and distribute it"""
from fabric.operations import local, run, put
from fabric.api import env, runs_once
from datetime import datetime
from os.path import exists, basename, getsize


env.hosts = ['18.212.205.195', '50.17.11.48']


@runs_once
def do_pack():
    """Generate the .tgz archive"""
    now = datetime.now()
    file = 'web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz'\
        .format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    local('mkdir -p versions')
    output = local('tar -cvzf versions/{} web_static'.format(file))
    if output.succeeded:
        print('web_static packed: versions/{} -> {}Bytes'
              .format(file, getsize('versions/{}'.format(file))))
        return 'versions/{}'.format(file)
    else:
        return None


def do_deploy(archive_path):
    """distribute the archive to the web servers"""
    if not exists(archive_path):
        return False
    archive = basename(archive_path)
    dir = archive.split('.')[0]
    res = put(archive_path, '/tmp/')
    if not res.succeeded:
        return False
    res = run('mkdir -p /data/web_static/releases/{}/'.format(dir))
    if not res.succeeded:
        return False
    res = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
              .format(archive, dir))
    if not res.succeeded:
        return False
    res = run('rm /tmp/{}'.format(archive))
    if not res.succeeded:
        return False
    res = run('mv /data/web_static/releases/{}/web_static/* '.format(dir) +
              '/data/web_static/releases/{}/'.format(dir))
    if not res.succeeded:
        return False
    res = run('rm -rf /data/web_static/releases/{}/web_static'.format(dir))
    if not res.succeeded:
        return False
    res = run('rm -rf /data/web_static/current')
    if not res.succeeded:
        return False
    res = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(dir))
    if not res.succeeded:
        return False
    print('New version deployed!')
    return True


def deploy():
    """generate the archive and deploy it"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
