#!/usr/bin/python3
"""
script that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.user = 'ubuntu'
env.hosts = ['107.23.168.84', '52.90.109.65']  # list of web servers


def deploy():
    """
    function that creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:  # if archive_path is None:
        return False
    return do_deploy(archive_path)  # deploy = do_pack() + do_deploy()