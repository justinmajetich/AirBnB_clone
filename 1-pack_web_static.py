#!/usr/bin/python3
"""
    generates a .tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        function to compress directory into .tgz archive
        Return: Success - '.tgz' archive path
                Failure - None
    """
    rn = datetime.now()
    rn = now.strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_' + rn + '.tgz'
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(path))

    if result.succeeded:
        return path
    return None
