#!/usr/bin/python3
"""Script Fabric that generates a .tgz from the content of webstatic"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """return the archive path if archive has been correctly
        generated
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None
