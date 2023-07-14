#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents
 of the web_static folder of your AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Returns the archive path if archive has been
    correctly gernerated else return None
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_pathh = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(archive_pathh))

    if tgz_archive.succeeded:
        local("chmod 664 versions/*")
        return archive_pathh
    else:
        return None
