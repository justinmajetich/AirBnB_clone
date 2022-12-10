#!/usr/bin/python3
"""Generate a .tgz archive"""
from fabric.operations import local
from datetime import datetime
from os.path import getsize


def do_pack():
    """Generate the .tgz archive"""
    now = datetime.now()
    file = 'web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz'\
        .format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    local('mkdir -p versions')
    output = local('tar -cvzf versions/{} web_static'.format(file))
    if output.succeeded:
        print('web_static packed: versions/{} -> {}Bytes'
              .format(file, getsize('versions/{}'.format(file))))
        return 'versions/{}'.format(file)
    else:
        return None
