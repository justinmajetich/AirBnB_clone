#!/usr/bin/python3
"""Clean all archives based on the number of
arguements passed"""

from operator import length_hint
from fabric.api import run, local, cd, env
import os

# env.hosts = ['18.234.193.94', '18.234.107.246']


def do_clean(number=0):
    """Cleans all .tgz files"""
    """if os.path.exists('versions'):
        # with cd('versions'):
        # local('find ')
        path = 'versions'
        files = [file for file in os.listdir(
            path) if 'web' in file and '.tgz' in file]

        print(files)

        length = len(files)
        if int(number) > length:
            exit
        if int(number) == 0 or int(number) == 1:
            last = 1
        else:
            last = int(number)

        if files:
            for index in range(length - last):
              local('rm versions/{}'.format(files[index]))"""

    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
