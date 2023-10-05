#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """this is a do pack fabric method"""
    dt = datetime.now()
    date = dt.strftime("%Y%m%d%H%M%S")
    file_path = ("versions/web_static_{}.tgz".format(date))

    if os.path.exists("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_path)).failed is True:
        return None
    return file_path
