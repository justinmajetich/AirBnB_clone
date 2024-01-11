#!/usr/bin/python3
"""Fab file for task 1"""

from datetime import datetime
from fabric.api import local, env
import os

env.warn_only = True


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static.

    Return:
        the name of the archive on success or None if faied.
    """
    now = datetime.now()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
    )
    print("Packing web_static into versions/{}".format(file_name))
    if not os.path.exists("versions"):
        os.mkdir("versions")
    status = local("tar -cvzf versions/{} web_static".format(file_name))

    if status.failed:
        return None
    return file_name
