#!/usr/bin/python3
"""genrate archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except:
        return None
