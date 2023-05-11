#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives, using the function do_clean:
    Prototype: def do_clean(number=0):
    number is the number of archives, including the most recent, to keep
      If number is 0 or 1, keep only the most recent version of your archive
      If number is 2, keep most & second most recent version of archives
    Your script should:
      Delete all unnecessary archives (minus the number to keep)
        in version and /data/web_static/releases folders of your servers
    Use env.hosts variable to execute remote commands on both servers
"""
from fabric.api import *

env.hosts = ['<34.234.193.7>', '<54.174.67.136>']
env.user = 'ubuntu'


def do_clean(number=0):
    """ Clean old unnecessary archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
