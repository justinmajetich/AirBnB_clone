#!/usr/bin/python3
"""
Just packing
"""
from datetime import datetime
from fabric.api import *
import tarfile

env.hosts = ['18.215.160.48', '34.201.174.39']


def do_pack():
    """compress before sending"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = local('mkdir -p versions/web_static_{}'.format(now))
    tar = local('tar -czvf versions/web_static_{}.tgz web_static'.format(now))
    file_name = "versions/web_static_{}.tgz".format(now)
    if file_name:
        return file_name
    else:
        return None


"""
Just Deploying
"""


def do_deploy(archive_path):
    """Deploy archive after compressing"""
    if not archive_path:
        return False
    try:
        with cd('/tmp'):
            res = put(archive_path, "/tmp")
            print(res)
        archive = archive_path.split("/")[-1]
        free = archive.split(".")[0]
        sudo('mkdir -p /data/web_static/releases/{}/'.format(free))
        sudo('tar -xzf /tmp/{} -C /data/web_static\
/releases/{}/'.format(archive, free))
        sudo('rm /tmp/{}'.format(archive))
        sudo('mv /data/web_static/releases/{}\
/web_static/* /data/web_static/releases/{}'.format(free, free))
        sudo('rm -rf /data/web_static/releases/{}/web_static'.format(free))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases\
/{}/ /data/web_static/current'.format(free))
        return True
    except:
    	return False


"""
Full deployment
"""


def deploy():
    """Based on 2 and Based on 1"""
    path = do_pack()
    if path is None:
        return False
    new_deploy = do_deploy(path)
    return new_deploy
