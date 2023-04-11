#!/usr/bin/python3

"""
This script hosts a function that packs the content of a file
"""


from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    '''Generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    tgz_pathname = 'versions/web_static_{}.tgz'.format(datetime.strftime(datetime.now(),
                                                    '%Y%m%d%H%M%S'))
    tar_ball_output = local("tar -czvf {} web_static".format(tgz_pathname))
    if tar_ball_output.failed:
        return None
    return tgz_pathname
