#!/usr/bin/python3
"""
Wites a fabric script to genereate tgz archive
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Makes an archive on web_static folder
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))
    if result is not None:
        return archive
    else:
        return None
