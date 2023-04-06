#!/usr/bin/python3
"""
Fabric script generates .tgz archive of all in web_static folder.
"""
from fabric.api import local
from datetime import datetime
from time import strftime


def do_pack():
    """generates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static/".format(file))
        return file
    except BaseException:
        return None
