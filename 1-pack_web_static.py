#!/usr/bin/python3
'''Fabric srcript that generates .tgz archive
    of static files'''

from fabric.api import local
from datetime import datetime
from fabric.decorators import run_once

@run_once
def do_pack():
    '''Generates .tgz archive from web_static contents'''
    local(mkdir -p varsions)
    path = ('versions/web_static_{}.tgz'.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local('tar -cvzf {} web_static'.format(path), capture=True)

    if result.failed:
        return None
    return path
