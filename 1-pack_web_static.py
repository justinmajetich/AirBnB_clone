#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents
 of the web_static folder of your AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Returns the archive path if archive has been 
    correctly gernerated else return None
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(archive_path))

    if tgz_archiv.succeeded:
        return archive_path
    else:
        return None
