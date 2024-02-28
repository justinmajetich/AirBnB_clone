#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ do_pack fonction """
    try:
        if not os.path.exists('versions'):
            local('mkdir -p versions')
        now = datetime.now()
        times = now.strftime('%Y%m%d%H%M%S')
        name = 'web_static_{}.tgz'.format(times)
        local('tar -cvzf versions/{} web_static'.format(name))

        return 'versions/{}'.format(name)
    except Exception as e:
        return None
