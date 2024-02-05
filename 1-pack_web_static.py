#!/usr/bin/python3
from fabric.api import local
from  datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(timestamp)
    result = local("tar -czvf versions/{} web_static".format(archive_name)

    if result.failed:
        return None

    return "version/{}".format(archive_name)
