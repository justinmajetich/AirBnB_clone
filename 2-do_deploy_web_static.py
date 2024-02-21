#!/usr/bin/python3

"""
Deploy the to a remote server
Usage: ./2_do_deploy_web_static.py do_deploy
"""

from fabric.api import env, task, put, run, sudo
from os import path

env.hosts = ['54.146.84.110', '100.26.156.138']
env.user = 'ubuntu'


@task(alias="deploy")
def do_deploy(archive_path) -> bool:
    """
    Deploy the application to the web servers
    Args:
        None
    Returns:
        True ( if all goes well)
        False (if something is not right)
    """
    if not path.exists(archive_path):
        return False
    try:
        arc = archive_path.split("/")
        base_loc = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base_loc))
        main_loc = "/data/web_static/releases/{}".format(base_loc)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main_loc))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main_loc, main_loc))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main_loc))
        return True
    except Exception:
        return False
