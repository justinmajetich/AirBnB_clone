#!/usr/bin/python3
"""
Fabric script method:
    do_deploy: deploys archive to webservers
Usage:
    fab -f 2-do_deploy_web_static.py
<<<<<<< HEAD
    do_deploy:archive_path=versions/web_static_20230710143917.tgz
    -i my_ssh_private_key -u ubuntu 
=======
    do_deploy:archive_path=versions/web_static_20220928193100.tgz
    -i my_ssh_private_key -u ubuntu
>>>>>>> b467aec91895e0e836b0c64ef44767cd6c1a9c6d
"""
from fabric.api import env, put, run
#import os.path
from os.path import exists
env.hosts = ["54.210.88.216", "52.205.99.41"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
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
    except:
        return False
