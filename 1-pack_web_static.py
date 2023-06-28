#!/usr/bin/python3
"""
    generates a .tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


from fabric.api import local
from datetime import datetime


def do_pack():
    """
        compress directory to .tgz archive
    """
    time = datetime.now()
    time = time.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + time + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
