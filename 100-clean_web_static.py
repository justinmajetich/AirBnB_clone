#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean.
"""

from fabric.api import env, run, local, lcd
from datetime import datetime
import os

env.hosts = ['54.172.84.26', '52.23.177.182']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """Deletes out-of-date archives"""
    try:
        number = int(number)
        if number < 0:
            return False

        if number == 0 or number == 1:
            number = 1

        local_archives = local("ls -tr versions", capture=True).split()
        web_server_archives = run("ls -tr /data/web_static/releases",
                                  capture=True).split()

        local_archives_to_delete = local_archives[:-number]
        web_server_archives_to_delete = web_server_archives[:-number]

        with lcd("versions"):
            for archive in local_archives_to_delete:
                local("rm -f {}".format(archive))

        for archive in web_server_archives_to_delete:
            run("rm -rf /data/web_static/releases/{}".format(archive))

        return True

    except Exception:
        return False
