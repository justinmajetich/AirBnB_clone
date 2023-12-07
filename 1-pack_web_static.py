#!/usr/bin/python3
""" A fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ A python function that generates a .tgz archive"""

    local('mkdir -p version')
    time = datetime.now()
    form = "%Y%m%d%H%M%S"

    path = 'versions/web_static_{}.tgz'.format(time.strtime(form))
    local('tar -cvzf {} web_static'.format(path))
    if result.failed:
        return None
    return path
