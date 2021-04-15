#!/usr/bin/python3
""" Fabric script """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates a .tgz file from the contents of 'web_static' folder"""
    now = datetime.now()
    local('mkdir -p versions')
    result = local('tar -cvzf versions/web_static_{}.tgz ./web_static/'.format(
        now.strftime('%Y%m%d%H%M%S')))
    if result.succeeded:
        return 'versions/web_static_{}.tgz web_static/'.format(
            now.strftime('%Y%m%d%H%M%S'))
    else:
        return None
