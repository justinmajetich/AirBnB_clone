#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import *
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
    number = int(number)
    if number < 1:
        number = 1
    else:
        number += 1

    with lcd('./versions'):
        local("ls -1t | tail -n +" + str(number) + " | xargs -I {} rm -- {}")
    with cd('/data/web_static/releases'):
        run("ls -1t | tail -n +" + str(number) + " | xargs -I {} rm -rf -- {}")
