#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import from fabric.api import env, lcd, cd, run, local
from os import path

env.hosts = ['54.158.79.124', '54.146.64.149']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    Deletes out-of-date archives from the web servers.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = max(int(number), 1)
    with lcd("versions"), cd("/data/web_static/releases"):
        local_archives = sorted(os.listdir("."))
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        archives_to_delete = local_archives[:-number] + remote_archives[:-number]
        [local("rm ./{}".format(a)) for a in local_archives if a in archives_to_delete]
        [run("rm -rf ./{}".format(a)) for a in remote_archives if a in archives_to_delete]
