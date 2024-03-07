#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
import os
from datetime import datetime

from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    dt = datetime.now()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        return os.path.join("versions", file_name)
    except Exception:
        return None
