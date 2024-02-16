#!/usr/bin/python3
"""
    script that generates '.tgz' archive from the contents of the 'web_static'
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        function to compress directory into .tgz archive
        Return: Success - '.tgz' archive path
                Failure - None
    """
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
