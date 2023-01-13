#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from contents
of the web_static folder.
All files in the folder web_static must be added to the final archive
name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if
the archive has been correctly generated.
Otherwise, it should return None
"""
import time
from fabric.api import local


def do_pack():
    """generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{:s}.tgz".\
            format(time.strftime("%Y%m%d%H%M%S"))
    except BaseException:
        return None
