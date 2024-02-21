#!/usr/bin/python3
"""
    This script distributes an archive to your web servers,
    using the function do_deploy:
"""
from fabric.api import *
import os
import re


env.user = 'ubuntu'
env.hosts = ['3.238.130.141', '	44.192.24.10']


def do_deploy(archive_path):
    """
        Deploys archive path to remote hosts
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        regex = r'\/(\w+).tgz$'
        pattern = re.findall(regex, archive_path)

        web_path = "/data/web_static/releases/{}".format(pattern[0])

        run("mkdir -p {}".format(web_path))
        # unpacking
        run("tar -xzf /tmp/{}.tgz -C {}".format(pattern[0], web_path))
        run("mv {}/web_static/* {}".format(web_path, web_path))
        run("rm -rf {}/web_static".format(web_path))
        run("rm /tmp/{}.tgz".format(pattern[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(web_path))

        # success
        print("New version deployed!")
        return True
    except Exception:
        return False
