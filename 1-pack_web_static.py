#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.operations import local, run
import os
from datetime import datetime


def do_pack():
    """Docstring
    """
    filename = 'web_static_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.tgz'
    try:
        if not os.path.isdir('versions'):
            local('mkdir versions')

        return local('tar -cvzf versions/{} web_static'.format(filename))
    except Exception:
        return None
