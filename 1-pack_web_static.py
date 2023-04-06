#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once


@runs_once
def do_pack():
    '''generates .tgz archive from web_static dir'''
    local("mkdir -p versions")
    filename = "web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    )
    path = "versions/{}".format(filename)
    result = local("tar -cvzf {} web_static".format(path))

    if result.failed:
        return None
    return path
