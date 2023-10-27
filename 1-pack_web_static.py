#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(archive_name))
    return archive_name
