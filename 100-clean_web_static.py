#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from os import path
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.158.79.124', '54.146.64.149']


def do_clean(number=0):
    """
    Deletes all unnecessary archives (all archives minus the number to keep)
    Args:
        number (int): The number of archives to keep.
    """
    number = int(number)
    if number < 1:
        number = 1
    else:
        number += 1

    with lcd('./versions'):
        local("rm $(ls -t | awk 'NR>" + str(number) + "')")
    with cd('/data/web_static/releases'):
        run("rm $(ls -t | awk 'NR>" + str(number) + "')")
