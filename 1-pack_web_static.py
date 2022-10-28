#!/usr/bin/python3
"""create archive module"""
from os.path import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """function to zip files"""
    try:
        new_date = datetime.now()
        new_date = new_date.strftime('%Y%m%d%H%M%S')
        archive = f"versions/web_static_{new_date}.tgz"
        if isdir('versions') is False:
            local('mkdir versions')
        print(f"Packing web_static to {archive}")
        var = local(f'tar -cvzf {archive} web_static')
        return archive
    except Exception:
        return None
