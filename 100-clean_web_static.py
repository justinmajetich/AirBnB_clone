#!/usr/bin/python3
"""This script (based on the file 3-deploy_web_static.py) deletes
out-of-date archives, using the function do_clean:"""


from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['35.185.108.180', '34.229.169.234']


def local_clean(number=0):
    """Local Clean"""
    _list = local('ls -1t versions', capture=True)
    _list = _list.split('\n')
    n = int(number)
    if n in (0, 1):
        n = 1
    print(len(_list[n:]))
    for i in _list[n:]:
        local('rm versions/' + i)


def remote_clean(number=0):
    """Remote Clean"""
    _list = run('ls -1t /data/web_static/releases')
    _list = _list.split('\r\n')
    print(_list)
    n = int(number)
    if n in (0, 1):
        n = 1
    print(len(_list[n:]))
    for i in _list[n:]:
        if i is 'test':
            continue
        run('rm -rf /data/web_static/releases/' + i)


def do_clean(number=0):
    """Fabric script that deletes aout of dates archives"""
    local_clean(number)
    remote_clean(number)
