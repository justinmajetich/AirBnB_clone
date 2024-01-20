#!/usr/bin/python3
"""Generate .tgz file from the contents of the web_static folder"""

from fabric import api
from datetime import datetime
import os


def do_pack():
    """Function to create tarball of webstatic files from the web_static
    folder in Airbnb_v2.

    Returns: path of .tgz file on success, None otherwise
    """
    with api.settings(warn_only=True):
        isdir = os.path.isdir('versions')
        if not isdir:
            mkdir = api.local('mkdir versions')
            if mkdir.failed:
                return None
        suffix = datetime.now().strftime('%Y%m%d%M%S')
        path = 'versions/web_static_{}.tgz'.format(suffix)
        tar = api.local('tar -cvzf {} web_static'.format(path))
        if tar.failed:
            return None
        size = os.stat(path).st_size
        print('web_static packed: {} -> {}Bytes'.format(path, size))
        return path
