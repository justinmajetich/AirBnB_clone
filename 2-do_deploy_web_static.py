#!/usr/bin/python3
"""
Deploy archive
"""
import os
from fabric.operations import run, put, sudo
from fabric.api import env
env.user = 'ubuntu'
env.hosts = ['18.215.160.48','34.201.174.39']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """A fabric script that distributes archive to your web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        put('archive_path', '/tmp')
        archive = archive_path.split('/')[-1]
        free = archive.strip('.tgz')
        sudo('mkdir -p /data/web_static/releases/{}'.format(free))
        run('cd /data/web_static/releases/{}'.format(free))
        sudo('tar xzvf archive_path')
        sudo('rm -f /data/web_static/current')
        sudo('ln -sf /data/web_static/releases/{} /data/web_static/current'.format(free))
        return True
    else:
        return False
