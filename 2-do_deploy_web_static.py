#!/usr/bin/python3
"""
Fabric file to generate Project Deploy Static
"""
from fabric.api import env, sudo, run, local, put

env.hosts = ['3.235.225.96', '34.236.187.99']


def do_deploy(archive_path):
    """
    Function to deploy the static website to all servers
    """
    file_name = archive_path.split('/')[-1][0:-4]
    if local("ls {}".format(archive_path)).failed:
        return False
    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p /data/web_static/releases/{}'.format(file_name)).failed:
        return False
    if sudo('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file_name, file_name)).failed:
        return False
    if sudo('chown -R {}:{} /data/web_static/releases/{}'
            .format(env.user, env.user, file_name)).failed:
        return False
    if run('mv /data/web_static/releases/{}/web_static/* /data/web_static/rel'
            'eases/{}'.format(file_name, file_name)).failed:
        return False
    if run('rm /tmp/{}.tgz'.format(file_name)).failed:
        return False
    if run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(file_name)).failed:
        return False
    print('New version deployed!')
    return True
