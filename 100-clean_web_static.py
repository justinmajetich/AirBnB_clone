#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives using the do_clean function.
"""
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.158.79.124', '54.146.64.149']


def do_clean(number=0):
    """
    Deletes all unnecessary archives (all archives minus the number to keep)
    in the versions folder and /data/web_static/releases folder of both web servers.
    Args:
        number (int): The number of archives to keep.
    """
    number = int(number)
    if number < 1:
        return
    elif number == 1:
        local('ls -1t versions/ | tail -n +2 | xargs -I {} rm versions/{}')
    else:
        local('ls -1t versions/ | tail -n +{} | xargs -I {} rm versions/{}'
              .format(number + 1, '{}'))
    with cd('/data/web_static/releases'):
        run('ls -1t | tail -n +{} | xargs -I {} rm -rf /data/web_static/releases/{}'
            .format(number + 1, '{}'))


def deploy():
    """Deploys the web_static content to the web servers"""
    # ... previous deploy code ...
    do_clean(2)
