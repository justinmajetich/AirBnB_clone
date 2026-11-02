#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder using the function do_pack
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local('mkdir -p versions')
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)
    fname = "versions/{}".format(name)
    archive_path = local("tar -cvzf {} web_static/".format(fname))
    if archive_path:
        return (archive_path)
    else:
        return None
