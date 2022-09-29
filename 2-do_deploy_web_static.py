#!/usr/bin/python3
"""
Fabric file to generate Project Deploy Static
"""
from fabric.api import *
from datetime import datetime

env.hosts = ['3.235.225.96', '34.236.187.99']


def do_pack():
    """
    Function to create the compressed file
    """
    curr_datetime = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = "./versions/web_static_" + curr_datetime + ".tgz"
    local("mkdir -p ./versions")
    if local("tar -cvzf " + path + " ./web_static").succeeded:
        return path
    return None


def do_deploy(archive_path):
    """
    Function to deploy the static website to all servers
    """
    file_name = archive_path.split('/')[-1][0:-4]
    if local("ls " + archive_path).failed:
        return False
    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p /data/web_static/releases/' + file_name).failed:
        return False
    if sudo('tar -xzf /tmp/' + file_name + '.tgz -C /data/web_static/releases/'
            + file_name).failed:
        return False
    if sudo('chown -R ' + env.user + ':' + env.user
            + ' /data/web_static/releases/' + file_name).failed:
        return False
    if run('mv -f /data/web_static/releases/' + file_name
            + "/web_static/* /data/web_static/releases/" + file_name).failed:
        return False
    if run('rm -rf /data/web_static/releases/' + file_name
            + '/web_static').failed:
        return False
    if run('rm /tmp/' + file_name + '.tgz').failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s /data/web_static/releases/' + file_name
            + '  /data/web_static/current').failed:
        return False
    return True
