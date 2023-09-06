#!/usr/bin/python3
"""This function compresses a folder with a .tgz extension"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir -p versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archivePath = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -czvf {} web_static'.format(archivePath))
        return archivePath
    except:
        return None
