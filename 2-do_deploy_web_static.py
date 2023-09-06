#!/usr/bin/python3
"""
    a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers, using
    the function do_deploy:
"""

from os.path import isdir
from fabric.api import local, put, run
from datetime import datetime as dt


def do_deploy(archive_path):
    """ a function that distributes an archive to web servers """
    try:
        if isdir('archive_path') is not True:
            return False

        put(archive_path, '/tmp/')

        location = '/data/web_static/releases/'
        run(f'tar -fvx {archive_path} {location}')

        run(f'rm -rf {archive_path}')

    except Exception:
        return False
    
