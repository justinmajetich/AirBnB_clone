#!/usr/bin/python3
"""This function compresses a folder with a .tgz extension"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -czvf {} web_static'.format(archive_path))
        return archive_path
