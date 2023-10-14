#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['3.88.108.94', '3.94.103.13']

def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        archive_file = archive_path.split("/")[-1]
        release_f = "/data/web_static/releases/".format(archive_file.split(".")[0])
        put(archive_path, '/tmp/')
      
        run('mkdir -p {}/'.format( release_f))
        run('tar -xzf /tmp/{} -C {}/'.format(archive_file, release_f))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(release_f))
        run('rm -rf {}/web_static'.format(release_f))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(release_f))
        return True
    except:
        return False
